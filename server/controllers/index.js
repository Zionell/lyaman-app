const transporter = require('../mailer');

class Controllers {
    async request(req, res) {
        try {
            const { name, email, comment } = req.body;
            const message = `
                         <h1>Заявка на обучение от ${name}.</h1>
                         <ul>
                            <li>
                                Почта: ${email}
                            </li>
                            <li>
                                Комментарий: ${comment}
                            </li>
                         </ul>
                        `;


            await transporter.verify();
            await transporter.sendMail({
                from: process.env.MAIL,
                to: process.env.MAIL,
                subject: 'Запись на занятие',
                html: message,
            });
            res.send('success');
        } catch (e) {
            res.send(e);
        }
    }
}

module.exports = new Controllers();
