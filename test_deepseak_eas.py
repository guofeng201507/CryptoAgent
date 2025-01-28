from openai import OpenAI

##### API 配置 #####
openai_api_key = "ZTNhNWUxMDAwMmJkMzkzM2RiMzE0ZDM0YTk2NTMwMzk5MmI1NzgxNg=="
openai_api_base = "http://1441377338211808.cn-hangzhou.pai-eas.aliyuncs.com/api/predict/quickstart_20250128_ds_r1_qwen14b/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id
print(model)


def main():

    stream = True

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "你好，介绍一下你自己，越详细越好。",
                    }
                ],
            }
        ],
        model=model,
        max_completion_tokens=1024,
        stream=stream,
    )

    if stream:
        for chunk in chat_completion:
            print(chunk.choices[0].delta.content, end="")
    else:
        result = chat_completion.choices[0].message.content
        print(result)


if __name__ == "__main__":
    main()