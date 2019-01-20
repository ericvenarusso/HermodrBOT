# HermodrBOT
This project was created to send promotions alerts on telegram.

## Files
1. <b> HermodrMain </b>: Send messages to the target users on Telegram.
2. <b> Crawler </b>: Web-Scraping a e-commerce site.
3. <b> Telegram </b>: Use the TelegramAPI to get the target users and send messages.

## How it works ?
First of all you will need to create a TelegramBOT and you can do this by sending a message to BotFather, for more information you can acess: <src>https://core.telegram.org/bots/api<src>. After creating your bot you will receive a token that will be going to used on the code execution to send the messages and get the target users.
  
The bot will get all the id_users that are in his conversation history and will send a custom mensage by Web Scrapping a product from a e-commerce site.

To execute the code you just need to execute the HermodrMain.
</br>
```python3 HermodrMain.py``` 
