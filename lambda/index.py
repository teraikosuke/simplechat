import json
import urllib.request

# ngrok URL
FASTAPI_URL = "https://a3ab-34-125-137-162.ngrok-free.app/predict"

def lambda_handler(event, context):
    try:
        # メッセージの取得
        body = json.loads(event['body'])
        message = body.get('message', '')

        # FastAPIへPOSTリクエストを送信
        req = urllib.request.Request(
            FASTAPI_URL,
            data=json.dumps({"message": message}).encode(),
            headers={"Content-Type": "application/json"}
        )

        with urllib.request.urlopen(req) as res:
            response_data = json.loads(res.read().decode())

        # FastAPIの応答を返す
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "success": True,
                "response": response_data.get("response", "")
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }
