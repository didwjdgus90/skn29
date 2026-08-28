import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

@csrf_exempt
def infer_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST 요청만 처리 가능합니다.'}, status=400)
        
    try:
        body = json.loads(request.body)
        user_input = body.get('prompt', '')
        
        if not user_input:
            return JsonResponse({'error': 'prompt가 누락되었습니다.'}, status=400)
            
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return JsonResponse({'error': '서버 환경 변수에 OPENAI_API_KEY 설정이 없습니다.'}, status=500)
            
        client = OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        
        output_text = response.choices[0].message.content
        
        return JsonResponse({
            'status': 'success',
            'model': 'gpt-5-nano',
            'response': output_text
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
