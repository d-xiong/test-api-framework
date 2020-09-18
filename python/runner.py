from flask import Flask, json, request

companies = [
    {
        "id": 1,
        "name": "Lorem Ipsums are the best."
    },
    {
        "id": 2,
        "name": "But did you know that there are other ones, and not limited to the basic one???"
    }
]
api = Flask(__name__)


@api.route('/test', methods=['GET'])
def get_companies():
    return json.dumps(companies)


@api.route('/test', methods=['POST'])
def post_companies():
    if request.method == 'POST':
        posted_data = request.get_json()
        companies.append(posted_data)
        return json.dumps({"success": True}), 201


if __name__ == '__main__':
    api.run()
