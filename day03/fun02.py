# 네비게이션
def set_navi(destination, route='최적길'):
    print(f'{destination}으로 안내를 시작합니다. (경로:{route})')

# 목적지만 말할때 (아무말안하면 최적길!)  
set_navi('강릉')   
# 특별히 다른길을 원할때(무료도로)
set_navi('강릉','무료도로')   
# 강릉을 가기위한 네비게이션 호출
set_navi(route='무료도로',destination='강릉')  