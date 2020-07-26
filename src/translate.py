import boto3

client = boto3.client('translate', region_name="us-west-2");
text = " привет, меня зовут Артем. Я прохожу курсы по devOps"
translation = client.translate_text(Text=text, SourceLanguageCode="auto", TargetLanguageCode="en")

print(translation["TranslatedText"])