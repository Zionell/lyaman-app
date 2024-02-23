/**
 * request service
 */

import {factories} from '@strapi/strapi';
import nodemailer from "nodemailer"

export default factories.createCoreService('api::request.request', ({strapi}) => ({
  async sendRequestLetter(data: {email: string, name: string, comment: string, publishedAt: Date}) {
    try {
      const transporter = nodemailer.createTransport({
        service: 'Yandex',
        auth: {
          user: process.env.EMAIL_HOST_USER,
          pass: process.env.EMAIL_HOST_PASSWORD,
        },
      });

      const html = `
       <h1>Привет!</h1> <br>
       <p>Тебе поступила заявка на консультацию от ${data.name}.</p>
       <p>Комментарий к сообщению от пользователя: ${data.comment}.</p>
       <p>Почта: ${data.email}.</p>
      `

      const options = {
        from: process.env.EMAIL_HOST_USER,
        to: process.env.EMAIL_HOST_USER,
        subject: 'Заявка на косультацию',
        html: html
      };

      return  transporter.sendMail(options);
    } catch (e) {
      console.warn('sendRequestLetter', e)
    }
  },

  async create(params) {
    try {
      const mail = await strapi.service('api::request.request').sendRequestLetter(params.data);

      const result = await super.create({
        data: {
          ...params.data,
          isSended: true
        }
      });

      return result;
    } catch (e) {
      console.warn('create', e)
    }
  },
}));
