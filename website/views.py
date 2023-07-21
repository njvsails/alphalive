from flask import Blueprint, render_template, flash, request, jsonify, redirect, url_for, session, current_app
from flask_login import login_required, current_user
from .models import Campaign, Document
from . import db
import json
import openai
import os

views = Blueprint('views', __name__)

@views.route('/dashboard', methods=['GET', 'POST'])
@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("dashboard.html")

from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain import LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.memory import ConversationBufferMemory, ChatMessageHistory

#initialisations for Live chat
chat = ChatOpenAI(temperature=1, openai_api_key='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')
history = ChatMessageHistory()

#initialisatons for Prompts
llm = OpenAI(model_name="text-davinci-003", openai_api_key='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')

@views.route('/campaign/all')
def campaigns():
    campaigns = Campaign.query.all()
    print(campaigns)
    return render_template('campaign_all.html', campaigns=campaigns)

@views.route('/campaign/manage/<int:campaign_id>', methods=['GET'])
def campaign_manage(campaign_id):
    campaign = Campaign.query.get(campaign_id)
    if not campaign:
        return redirect(url_for('campaigns'))  # Redirect to campaigns list if the campaign was not found
    documents = Document.query.filter_by(campaign_id=campaign_id).all()
    return render_template('campaign_manage.html', campaign=campaign, documents=documents, campaign_id=campaign_id)

@views.route('/document/delete/<int:document_id>', methods=['DELETE'])
def delete_document(document_id):
    document = Document.query.get_or_404(document_id)
    db.session.delete(document)
    db.session.commit()
    return jsonify({'message': 'Document deleted'}), 200

@views.route('/campaign/delete/<int:campaign_id>', methods=['GET', 'POST', 'DELETE'])
def delete_campaign(campaign_id):
    # Get the campaign
    campaign = Campaign.query.get_or_404(campaign_id)
    
    # Delete associated documents
    Document.query.filter_by(campaign_id=campaign.id).delete()
    
    # Delete the campaign
    db.session.delete(campaign)
    
    # Commit the changes to the database
    db.session.commit()
    
    # Redirect the user to the main page
    return jsonify({'message': 'Campaign deleted'}), 200


from datetime import datetime

@views.route('/campaign/rental', methods=['GET', 'POST'])
def rental_campaign():
    if request.method == 'POST':
        # Extract form data
        form_data = request.get_json()

        # Convert market_date string to date object
        date_string = form_data.get('marketDate')
        date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
        
        # Create a new campaign
        new_campaign = Campaign(
            property_address=form_data.get('propertyAddress'),
            rental_amount=form_data.get('rentalAmount'),
            sales_price=None,
            home_size=None, 
            type='rental',
            market_date=date_object,  # replace string with date object
            property_type=form_data.get('propertyType'),
            bedrooms=form_data.get('bedrooms'),
            bathrooms=form_data.get('bathrooms'),
            car_spaces=form_data.get('carSpaces'),
            furnishing=form_data.get('furnishing'),
            airconditioning=form_data.get('airconditioning'),
            pet_friendly=form_data.get('petFriendly'),
            amenity_pool=form_data.get('propertyAmenities', {}).get('amenityPool'),
            amenity_gym=form_data.get('propertyAmenities', {}).get('amenityGym'),
            amenity_spa=form_data.get('propertyAmenities', {}).get('amenitySpa'),
            amenity_communal_entertaining=form_data.get('propertyAmenities', {}).get('amenityCommunalEntertaining'),
            amenity_communal_cooking=form_data.get('propertyAmenities', {}).get('amenityCommunalCooking'),
        )

        db.session.add(new_campaign)
        db.session.commit()

        print("campaign: ", new_campaign.id)

        return jsonify({'message': 'Campaign successfully created', 'redirect': url_for('views.rental_select', campaign_id=new_campaign.id)}), 201

    return render_template('campaign_rental.html')

@views.route('/campaign/sale', methods=['GET', 'POST'])
def sales_campaign():
    if request.method == 'POST':
        # Extract form data
        form_data = request.get_json()

        # Convert market_date string to date object
        date_string = form_data.get('marketDate')
        date_object = datetime.strptime(date_string, '%Y-%m-%d').date()

        # Create a new campaign
        new_campaign = Campaign(
            property_address=form_data.get('propertyAddress'),
            rental_amount=None,
            sales_price=form_data.get('salesAmount'),
            home_size=form_data.get('homeSize'),
            type='sales',
            market_date=date_object,  # replace string with date object
            property_type=form_data.get('propertyType'),
            bedrooms=form_data.get('bedrooms'),
            bathrooms=form_data.get('bathrooms'),
            car_spaces=form_data.get('carSpaces'),
            furnishing=form_data.get('furnishing'),
            airconditioning=form_data.get('airconditioning'),
            pet_friendly=form_data.get('petFriendly'),
            amenity_pool=form_data.get('propertyAmenities', {}).get('amenityPool'),
            amenity_gym=form_data.get('propertyAmenities', {}).get('amenityGym'),
            amenity_spa=form_data.get('propertyAmenities', {}).get('amenitySpa'),
            amenity_communal_entertaining=form_data.get('propertyAmenities', {}).get('amenityCommunalEntertaining'),
            amenity_communal_cooking=form_data.get('propertyAmenities', {}).get('amenityCommunalCooking'),
        )

        db.session.add(new_campaign)
        db.session.commit()

        print("campaign: ", new_campaign.id)

        return jsonify({'message': 'Campaign successfully created', 'redirect': url_for('views.sales_select', campaign_id=new_campaign.id)}), 201

    return render_template('campaign_sale.html')


def reset_database(app):
    with app.app_context():
        db.reflect()
        db.drop_all()
        db.create_all()
    print('Reset Database!')

@views.route('/resetdb')
def reset_db_route():
    reset_database(current_app)  # current_app is a Flask global
    return "Database reset completed!"

@views.route('/campaign/rental/select/<int:campaign_id>', methods=['GET', 'POST'])
def rental_select(campaign_id):
    current_campaign = Campaign.query.get(campaign_id)
    campaigns = Campaign.query.all()  # get all campaigns
    if request.method == 'POST':
        # Extract form data
        form_data = request.form

        # Create a new Document with all the input data
        document = Document(
            campaign_id=campaign_id,
            document_name=form_data.get('document_name'),
            document_type=form_data.get('document_type'),
            include_agent_contact=bool(form_data.get('include_agent_contact')),
            agent_name=form_data.get('agent_name'),
            agent_email=form_data.get('agent_email'),
            agent_mobile=form_data.get('agent_mobile'),
            content=''  # initialize content with empty string
        )
        db.session.add(document)
        db.session.commit()

        # Now you can update the 'content' field with your API output
        # Simulate getting the output of an API call
        api_output = document_rental(document.id)
        document.content = api_output  # update content
        db.session.commit()  # commit changes again

        return redirect(url_for('views.document_screen', document_id=document.id))

    return render_template('campaign_rental_select.html', current_campaign=current_campaign, campaigns=campaigns)

@views.route('/campaign/sale/select/<int:campaign_id>', methods=['GET', 'POST'])
def sales_select(campaign_id):
    current_campaign = Campaign.query.get(campaign_id)
    campaigns = Campaign.query.all()  # get all campaigns
    if request.method == 'POST':
        # Extract form data
        form_data = request.form

        # Create a new Document with all the input data
        document = Document(
            campaign_id=campaign_id,
            document_name=form_data.get('document_name'),
            document_type=form_data.get('document_type'),
            include_agent_contact=bool(form_data.get('include_agent_contact')),
            agent_name=form_data.get('agent_name'),
            agent_email=form_data.get('agent_email'),
            agent_mobile=form_data.get('agent_mobile'),
            content=''  # initialize content with empty string
        )
        db.session.add(document)
        db.session.commit()

        # Now you can update the 'content' field with your API output
        # Simulate getting the output of an API call
        api_output = document_sales(document.id)
        document.content = api_output  # update content
        db.session.commit()  # commit changes again

        return redirect(url_for('views.document_screen', document_id=document.id))

    return render_template('campaign_sale_select.html', current_campaign=current_campaign, campaigns=campaigns)


from .prompts import sales_social, sales_email, sales_property, rent_email, rent_property, rent_social

def document_rental(document_id):
    document = Document.query.get_or_404(document_id)
    campaign = Campaign.query.get_or_404(document.campaign_id)
    template = ''

    if document.document_type == "Property Listing Advertisement":
        template = rent_property
    elif document.document_type == "Social Media Post":
        template = rent_social
    else:
        template = rent_email

    prompt = PromptTemplate(
        input_variables=["address", "rent", "date", "type", "bedrooms", "bathrooms", "parking"],
        template=template,
    )

    output = llm(prompt.format(address=campaign.property_address, rent=campaign.rental_amount, date=campaign.market_date, type=campaign.property_type, bedrooms=campaign.bedrooms, bathrooms=campaign.bathrooms, parking=campaign.car_spaces))

    return output

def document_sales(document_id):
    document = Document.query.get_or_404(document_id)
    campaign = Campaign.query.get_or_404(document.campaign_id)
    template = ''

    if document.document_type == "Property Listing Advertisement":
        template = sales_property
    elif document.document_type == "Social Media Post":
        template = sales_social
    else:
        template = sales_email

    prompt = PromptTemplate(
        input_variables=["address", "price", "size", "date", "type", "bedrooms", "bathrooms", "parking"],
        template=template,
    )

    output = llm(prompt.format(address=campaign.property_address, price=campaign.sale_price, size=campaign.home_size, date=campaign.market_date, type=campaign.property_type, bedrooms=campaign.bedrooms, bathrooms=campaign.bathrooms, parking=campaign.car_spaces))

    return output


@views.route('/document/<int:document_id>', methods=['GET'])
def document_screen(document_id):
    # Retrieve the document from the database
    document = Document.query.get(document_id)

    # If the document is not found, redirect to dashboard or a suitable error page
    if document is None:
        flash('Document not found.', category='error')
        return redirect(url_for('views.dashboard'))

    return render_template('document_screen.html', document=document)


@views.route('/campaign/new', methods=['GET', 'POST'])
def campaign_new():
    if request.method == 'POST':
        if 'form_type' in request.form:
            form_type = request.form.get('form_type')
        
            if form_type == 'rental':
                rental_data = {
                    'salesFocus': request.form.get('salesFocus'),
                    'rentalAmount': request.form.get('rentalAmount'),
                    'autopopulatedField': request.form.get('autopopulatedField'),
                    'marketDate': request.form.get('marketDate')
                }
                # Process rental form data and return the URL for the rental success page
                redirect_url = url_for('views.rental_success', **rental_data, _external=True, _scheme='http')
                return jsonify({'redirect': redirect_url})
            
            elif form_type == 'sales':
                sales_data = {
                    'salesFocus': request.form.get('salesFocus'),
                    'salesAmount': request.form.get('salesAmount'),
                    'propertyStatus': request.form.get('propertyStatus')
                }
                # Process sales form data and return the URL for the sales success page
                redirect_url = url_for('views.sales_success', **sales_data, _external=True, _scheme='http')
                return jsonify({'redirect': redirect_url})

    return render_template("campaign_new.html")


@views.route('/campaign')
def campaign():
    return render_template("campaign_home.html")

@views.route('/assistant')
@login_required
def assistant():
    return render_template("ai_chatbot.html")

@views.route('/api/chatbot', methods=['GET', 'POST'])
@login_required
def chatbot():
    user_message = request.form.get('text')
    history.add_user_message(user_message)
    ai_response = chat(history.messages)
    print(ai_response.content)
    history.add_ai_message(ai_response.content)
    return jsonify(text=ai_response.content)

@views.route('/postcode')
def postcode():
    return render_template('postcode.html')

@views.route('/api/chat_gpt', methods=['POST'])
def chat_gpt():
    print("Request received.")  # Debugging print statement
    input_number = request.form.get('inputNumber')
    prompt = f"""You are a helpful assistant. Using the postcode {input_number}, please assist with providing and the following information.


3 suburb names that attach to that post code listed in order by most commonly used
Ranged Average Apartment & House Rental Amounts in price per week.
Ranged Average Apartment & House Sale Prices
Provide the distance of the post code from the CBD
Ranged Average Income per household for provided postcode
3 most represented race demographic of peoples displayed in the format demographic(%)


Describe the livability of the given post code in relation to all other suburbs in Australia in the format of “Livability: one word and a score out of 10”
Describe the Transportation of the given post code in relation to all other suburbs in Australia in the format of “Transportation: one word and a score out of 10”
Describe the educational amenities of the given postcode in relation to all other suburbs in Australia in the format of “Education: one word and a score out of 10”
Describe the entertainment amenities of the given postcode in relation to all other suburbs in Australia in the format of “Entertainment: one word and a score out of 10”
Describe the crime rate of the given postcode in the format of “Property Safety: only as a one word and a score out of 10” where 1 is the highest crime rate


Please provide the 3 most popular entertainment locations in the post code
Please Provide a list of every childrens educational amenity in the given postcodes catchment and if that enmity is private or public in brackets after it

Provide the information in a neat form with paragraphs and dot points similar to how my requests are set out.
"""   
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,  # Increase this value for more paragraphs of text
            n=1,
            stop=None,
            temperature=0.7
        )
        message = response.choices[0].text.strip()
    except Exception as e:
        message = str(e)

    print(f"Message: {message}")  # Debugging print statement
    return jsonify({'outputText': message})


# #removes memory if too big a history
# class TruncatedChatHistory(ChatMessageHistory):
#     MAX_TOKENS = 2048  # Set this to your model's maximum token limit

#     def add_message(self, role, content):
#         message = ChatMessageTemplate(role, content)
#         self.messages.append(message)

#         while self.token_count() > self.MAX_TOKENS:
#             self.messages.pop(0)  # remove the earliest message

#     def token_count(self):
#         return sum(message.token_count() for message in self.messages)