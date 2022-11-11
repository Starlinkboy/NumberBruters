const prompt = require('prompt-sync')({ sigint: true });
const { greenBright, cyanBright, magentaBright, red, blueBright } = require("colorette");
const Discord = require("discord.js");
const { WebhookClient } = require('discord.js');
const a = 6969
const b = 10000
let attempts = 0

const webhook = prompt(blueBright("Enter Webhook Url: "))
console.log(magentaBright("Starting Bruter..."))
const myHook = new WebhookClient({ url: webhook });


var startTime = new Date();

while (true) {

  attempts = attempts + 1
  const c = Math.floor(Math.random() * b);
  console.log(cyanBright(c))

  if (c == a) {
    var endTime = new Date();


    var time = endTime - startTime;


    var etime = time / 1000;
    var metime = time / 60;
    var hetime = time / 3600

    if (etime < 60) {
      const embed = new Discord.MessageEmbed()
        .setTitle("Number Bruted")
        .setDescription(`Number to brute: ${a}\nNumber to be bruted from: ${b}\nAttempts: ${attempts}\nTime Elapsed:\n-Seconds: ${etime}`)
        .setColor("#0000FF")
      myHook.send({ embeds: [embed], username: 'Number Bruter JavaScript', avatarURL: 'https://i.imgur.com/z6j9cas.png', }).catch(console.error);
    }
    else if (etime < 3600) {
      const embed = new Discord.MessageEmbed()
        .setTitle("Number Bruted")
        .setDescription(`Number to brute: ${a}\nNumber to be bruted from: ${b}\nAttempts: ${attempts}\nTime Elapsed:\n-Seconds: ${etime}\n-Minutes: ${metime}`)
        .setColor("#0000FF")
      myHook.send({ embeds: [embed], username: 'Number Bruter JavaScript', avatarURL: 'https://i.imgur.com/z6j9cas.png', }).catch(console.error);
    }
    else {
      const embed = new Discord.MessageEmbed()
        .setTitle("Number Bruted")
        .setDescription(`Number to brute: ${a}\nNumber to be bruted from: ${b}\nAttempts: ${attempts}\nTime Elapsed:\n-Seconds: ${etime}\n-Minutes: ${metime}\n-Hours: ${hetime}`)
        .setColor("#0000FF")
      myHook.send({ embeds: [embed], username: 'Number Bruter JavaScript', avatarURL: 'https://i.imgur.com/z6j9cas.png', }).catch(console.error);
    }





    console.log(greenBright(`Number bruted after ${attempts} attempts.`))
    console.log(red("Bruter Information sent on Webhook"))


    break;

  }
}