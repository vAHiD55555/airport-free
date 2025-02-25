import requests

def get_first_url():
    # API URL
    api_url = "https://api.akams.cn/github"
    
    try:
        # 发送GET请求
        response = requests.get(api_url)
        # 检查请求是否成功
        response.raise_for_status()
        
        # 解析返回的JSON数据
        json_data = response.json()
        
        # 检查data字段是否存在且不为空
        if 'data' in json_data and len(json_data['data']) > 0:
            # 获取第一个元素中的url字段
            first_url = json_data['data'][0]['url']
            print(first_url)
        else:
            print("httpsa://github.moeyy.xyz")
    
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")

if __name__ == "__main__":
    get_first_url()
