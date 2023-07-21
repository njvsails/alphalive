# Prompting section. This section will contain all the prompt strings for the different tools

sales_social = """
Pretext:
For the purposes of this request - you are to construct language in the specified formats as if you were a real estate agent based in Australia looking to "SELL" a property in Australia.
This request requires you to construct advertising, promotional and informational text based on both information provided and information already available to you about the post code in any given address.
Do NOT produce example text until you have been provided with a property address and all information required.

Address:
{address}

Property Sale Conditions:
The date this property is on the market is {date}
The Sale Price of the Property is {price}
The market status this property is {status}

Property Details:
The type of Property is a {type}
This property size is {size}
The number of bedrooms in the property is {bedrooms}
The number of bathrooms in the property is {bathrooms}
The number of parking spaces for vehicles in the property is {parking}

Text Output Information:
The Block of text must include all of the "PROPERTY DETAILS" in list form as a summary and any additional information required to make the property sound as appealing as possible to a potential customer.

Please Select the "PLATFORM" for this text:
Facebook

Please make the "WRITING TONE" of this Text
“Premium Residential” - Use reserved and personal language with an emphasis on livability and lifestyle experience.

Please make the "CREATIVE VIBE" of this text:
“Positive Neutral” - Use soft, warm and structured language with an emphasis on inclusion and support.

Please adhere strictly to a "LONG" by using the maximum post length available for the chosen social media platform.

Please use the selected platform limitations, defined writing, creative parameters and word limit criteria to create a "SOCIAL MEDIA POST" with relevant emojis and hashtags to best promote the property as well as the key features of the property
Please use all of the above provided details & include relevant information about the suburb based on the post code.
"""

sales_email = """ 
Pretext:
For the purposes of this request - you are to construct language in the specified formats as if you were a real estate agent based in Australia looking to "SELL" a property in Australia.
This request requires you to construct advertising, promotional and informational text based on both information provided and information already available to you about the post code in any given address.
Do NOT produce example text until you have been provided with a property address and all information required.

Address:
{address}

Property Sale Conditions:
The date this property is on the market is {date}
The Sale Price of the Property is {price}
The market status this property is {status}

Property Details:
The type of Property is a {type}
This property size is {size}
The number of bedrooms in the property is {bedrooms}
The number of bathrooms in the property is {bathrooms}
The number of parking spaces for vehicles in the property is {parking}

Text Output Information:
The Block of text must include all of the "PROPERTY DETAILS" in list form as a summary and any additional information required to make the property sound as appealing as possible to a potential customer.

Please make the "WRITING TONE" of this Text
“Premium Residential” - Use reserved and personal language with an emphasis on livability and lifestyle experience.

Please make the "CREATIVE VIBE" of this text:
“Positive Neutral” - Use soft, warm and structured language with an emphasis on inclusion and support.

Please adhere strictly to a "LONG" by using the maximum post length available for the chosen social media platform.

Please construct a promotional email in full structure including a generalised greeting, introduction to the property, block of sales text selling the property and a friendly signoff and farewell.
Please use all of the above provided details & include relevant information about the suburb based on the post code
"""

sales_property = """
Pretext:
For the purposes of this request - you are to construct language in the specified formats as if you were a real estate agent based in Australia looking to "SELL" a property in Australia.
This request requires you to construct advertising, promotional and informational text based on both information provided and information already available to you about the post code in any given address.
Do NOT produce example text until you have been provided with a property address and all information required.

Address:
{address}

Property Sale Conditions:
The date this property is on the market is {date}
The Sale Price of the Property is {price}
The market status this property is {status}

Property Details:
The type of Property is a {type}
This property size is {size}
The number of bedrooms in the property is {bedrooms}
The number of bathrooms in the property is {bathrooms}
The number of parking spaces for vehicles in the property is {parking}

Text Output Information:
The Block of text must include all of the "PROPERTY DETAILS" in list form as a summary and any additional information required to make the property sound as appealing as possible to a potential customer.

Please make the "WRITING TONE" of this Text
“Premium Residential” - Use reserved and personal language with an emphasis on livability and lifestyle experience.

Please make the "CREATIVE VIBE" of this text:
“Positive Neutral” - Use soft, warm and structured language with an emphasis on inclusion and support.

Please adhere strictly to a "LONG" maximum word limit of 500 words

Please construct a block of text to appear on the sale advertisement for this property.
Please use all of the above provided details & include relevant information about the suburb based on the post code 
"""

rent_social = """ 
Pretext:
For the purposes of this request - construct language in the specified formats as if you were a real estate agent based in Australia looking to "RENT OUT" a property in Australia.
This request requires you to construct advertising, promotional and informational text based on both information provided and information already available to you about the post code in any given address.
Do NOT produce example text until you have been provided with a property address and all information required.

Address:
{address}

Property Rental Conditions:
The Weekly price of rent for this property is {rent}
The date this property is available to rent is {date}

Property Details:
The type of Property is a {type}
The number of bedrooms in the property is {bedrooms}
The number of bathrooms in the property is {bathrooms}
The number of parking spaces for vehicles in the property is {parking}

Text Output Information:
The Block of text must include all of the "PROPERTY DETAILS" in list form as a summary and any additional information required to make the property sound as appealing as possible to a potential customer.

Please make the "WRITING TONE" of this Text
“Premium Residential” - Use reserved and personal language with an emphasis on livability and lifestyle experience.

Please make the "CREATIVE VIBE" of this text:
“Positive Neutral” - Use soft, warm and structured language with an emphasis on inclusion and support.

Please adhere strictly to a "LONG" maximum word limit of 500 words

Please use the selected platform limitations, defined writing, creative parameters and word limit criteria to create a "SOCIAL MEDIA POST" with relevant emojis and hashtags to best promote the property as well as the key features of the property
Please use all of the above provided details & include relevant information about the suburb based on the post code.
"""

rent_email = """ 
Pretext:
For the purposes of this request - construct language in the specified formats as if you were a real estate agent based in Australia looking to "RENT OUT" a property in Australia.
This request requires you to construct advertising, promotional and informational text based on both information provided and information already available to you about the post code in any given address.
Do NOT produce example text until you have been provided with a property address and all information required.

Address:
{address}

Property Rental Conditions:
The Weekly price of rent for this property is {rent}
The date this property is available to rent is {date}

Property Details:
The type of Property is a {type}
The number of bedrooms in the property is {bedrooms}
The number of bathrooms in the property is {bathrooms}
The number of parking spaces for vehicles in the property is {parking}

Text Output Information:
The Block of text must include all of the "PROPERTY DETAILS" in list form as a summary and any additional information required to make the property sound as appealing as possible to a potential customer.

Please make the "WRITING TONE" of this Text
“Premium Residential” - Use reserved and personal language with an emphasis on livability and lifestyle experience.

Please make the "CREATIVE VIBE" of this text:
“Positive Neutral” - Use soft, warm and structured language with an emphasis on inclusion and support.

Please adhere strictly to a "LONG" maximum word limit of 500 words

Please construct a promotional email in full structure including a generalised greeting, introduction to the property, block of sales text selling the property and a friendly signoff and farewell.
Please use all of the above provided details & include relevant information about the suburb based on the post code
"""

rent_property = """
Pretext:
For the purposes of this request - construct language in the specified formats as if you were a real estate agent based in Australia looking to "RENT OUT" a property in Australia.
This request requires you to construct advertising, promotional and informational text based on both information provided and information already available to you about the post code in any given address.
Do NOT produce example text until you have been provided with a property address and all information required.

Address:
{address}

Property Rental Conditions:
The Weekly price of rent for this property is {rent}
The date this property is available to rent is {date}

Property Details:
The type of Property is a {type}
The number of bedrooms in the property is {bedrooms}
The number of bathrooms in the property is {bathrooms}
The number of parking spaces for vehicles in the property is {parking}

Text Output Information:
The Block of text must include all of the "PROPERTY DETAILS" in list form as a summary and any additional information required to make the property sound as appealing as possible to a potential customer.

Please make the "WRITING TONE" of this Text:
“Positive Neutral” - Use soft, warm and structured language with an emphasis on inclusion and support.
“Premium Residential” - Use reserved and personal language with an emphasis on livability and lifestyle experience.
Please adhere strictly to a "LONG" maximum word limit of 500 words - NOT including the text in conditions and disclaimers.

Please construct a block of text to appear on the rental advertisement for this property. 
Please use all of the above provided details & include relevant information about the suburb based on the post code
"""