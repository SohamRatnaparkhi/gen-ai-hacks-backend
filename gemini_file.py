import google.generativeai as genai
import PIL.Image
import json
from dotenv import load_dotenv
import os 

load_dotenv()

prompt1 = """Create a detailed prompt for an AI image generator to produce a visually striking, theme-oriented product banner. The theme is [Insert user-provided theme, e.g., 'Independence Day of India']. Incorporate the following elements:
Product and theme description: for holi
Enhanced themed offer: 15percent offer
Color palette: holi colors
Guidelines for the prompt:
Describe the desired layout and composition of the banner, emphasizing how it should prominently feature key symbols and colors associated with the theme (e.g., for Independence Day of India, include the Indian flag, saffron, white, and green colors, and patriotic symbols)
Specify how the product should be portrayed in relation to the theme, integrating it seamlessly with thematic elements
Indicate where and how the themed offer text should appear, possibly incorporating theme-related typography or design elements
Detail how the color palette should be utilized, ensuring it complements the theme's traditional colors
Explain how the theme should dominate the overall design, including specific instructions for incorporating iconic imagery, patterns, or motifs associated with the theme
Suggest additional graphic elements or visual effects that enhance the thematic presentation (e.g., fireworks for Independence Day, traditional patterns, or historical landmarks)
Specify the desired style and mood of the banner, ensuring it aligns with both the product and the celebratory or cultural significance of the theme
Include instructions for incorporating theme-specific symbols, icons, or cultural elements, providing examples relevant to the given theme
If applicable, suggest ways to blend modern and traditional elements to create a contemporary yet culturally relevant design
Craft a comprehensive prompt that will guide the AI image generator to create a cohesive, attractive, and effective product banner that seamlessly integrates the product, offer, and theme. Ensure that the theme is unmistakably represented through visual elements, creating a banner that resonates with the cultural or celebratory context while effectively promoting the product"""


genai.configure(api_key=os.environ.get("GEMINI_FLASH_API_KEY"))

def get_prompt(image,user_pref,lightening = False):
  img = PIL.Image.open(image)
  # img = "image_grid.jpg"

  # genai.configure(api_key=params['gemini'])

  # Set up the model
  if lightening==False:
    prompt1 = f"""Generate a prompt for creative and visually appealing dynamic banner prompt for promotional purposes based on the provided user prefference which is {user_pref}, including a product image, promotional offer, color palette, and theme. The banner should be engaging, reflect the audience's needs, and maintain brand consistency.
  Variables:
  Product Image: The image of the product being promoted (provided by the user).
  Promotional Offer: Text for the discount or special offer (e.g., "20% OFF", "Buy 1 Get 1 Free").
  Color Palette: A set of colors provided by the user to ensure brand consistency.
  Theme: The user-defined theme (e.g., festival-based, event-based, seasonal, etc.).
  Target Audience: Characteristics of the target audience (e.g., family-oriented, young adults, professionals).
  Instruction Steps:
  Base Layout:

  Position the product image at the center or prominently in the banner, ensuring that it remains the focal point.
  Surround the product with elements that reflect the given theme (e.g., festive colors, event-based symbols, seasonal imagery).
  The banner should maintain a clear and uncluttered structure to ensure that the product and promotional message stand out.
  Incorporate Promotional Offer:

  Display the promotional offer in a large, bold font in a noticeable area, such as the top-right or bottom-right of the banner.
  The offer text should be enclosed in a vibrant badge or box that contrasts well with the background but remains aligned with the brand’s color palette.
  Color Palette Consistency:

  Use the provided color palette to design the background, text, and other visual elements, ensuring consistency with the brand's identity.
  The colors should be used strategically to create visual balance without overwhelming the viewer. For example:
  Background gradient or splashes based on the brand colors.
  Text in contrasting colors to ensure readability.
  Subtle highlights and shadows to make the product and promotional elements pop.
  Theme Alignment:

  Incorporate design elements that reflect the user-provided theme. For example:
  If the theme is festival-based (e.g., Holi), use bright colors, splashes, and playful patterns.
  For an event-based theme (e.g., Independence Day), use national colors, celebratory symbols (like flags or lights).
  If the theme is seasonal, reflect elements like snowflakes for winter, flowers for spring, etc.
  Text and Fonts:

  Use bold, clean fonts for the promotional offer and tagline, ensuring readability.
  If a tagline is provided, place it beneath or near the product image in a contrasting color, using a fun, engaging font that aligns with the audience and theme.
  Make sure the font colors are chosen from the palette, ensuring they remain readable against the background.
  Lighting & Visual Effects:

  Apply soft lighting effects to the product image to enhance its clarity and make it visually appealing.
  Add subtle glow, shadows, or highlights around key elements like the product and promotional offer to create a sense of depth.
  Incorporate gentle gradients or splashes of colors to provide movement and energy to the banner, especially if the theme is dynamic like a festival.
  Final Branding and Logo:

  Place the brand logo in a visible but non-intrusive position (e.g., top-left or top-right), ensuring it doesn't overshadow the product image or promotional offer.
  Ensure the logo is well-lit and clearly visible against the background.
  Target Audience Adaptation:

  The overall design, colors, fonts, and theme should be aligned with the target audience. For example:
  If the audience is family-oriented, use playful, warm, and vibrant colors with cheerful imagery.
  For a more professional audience, opt for clean, minimalistic design with structured typography and subtle colors.
  """
  else:
    prompt1 = """giving lighting information of given image  """

  generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
  }

  model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                generation_config=generation_config)


  prompt_parts = [
    f"""{prompt1}""",img
  ]

  response = model.generate_content(prompt_parts)
  print(response.text)
  return response.text

user_pref = """attached is a given product , its for hollowine offer of cleaning"""
image = "back.jpg"
get_prompt(image,user_pref,lightening=True)
