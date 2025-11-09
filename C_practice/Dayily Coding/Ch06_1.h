Element data[MAX_SIZE];
int size = 0;
int sum = 0;

void error(char str[])
{
    printf("%s\n", str);
    exit(1);
}

void init_list() {size = 0;}
int is_empty() {return size == 0;}
int is_full() {return size == MAX_SIZE;}

void insert(int pos, Element e)
{
    if (is_full())
        error("다 찼다 그만 처 넣어라");

    if (pos < 0 || pos > size)
        error("이상한데 처 넣노 정신차려라");

    for (int i = size-1; i >= pos; i--)
        data[i+1] = data[i];
    data[pos] = e;
    size += 1;
}

Element delete(int pos)
{
    if (is_empty())
        error("값 없으니깐 꺼저");

    if (pos < 0 || pos >= size)
        error("이상한데 처 넣노 정신차려라");

    Element e = data[pos];
    for (int i = pos+1; i < size; i++)
        data[i-1] = data[i];
    size -= 1;
    return e;
}

Element get_entry(int pos)
{
    if (is_empty())
        error("값 없으니깐 꺼저");

    if (pos < 0 || pos >= size)
        error("이상한데 처 넣노 정신차려라");

    return data[pos];
}

void append(Element e) {
    insert(size, e);
}

Element pop() {
    return delete(size - 1);
}

void replace(int pos, Element e) {
    if (pos < 0 || pos >= size)
        error("이상한데 처 넣노 정신차려라");
    data[pos] = e;
}

int find1(Element e){
    for(int i = 0; i < size; i++)
        if (data[i] == e)
            return i;
    return -1;
}

int find2(int start, Element e) {
    for(int i = start; i < size; i++)
        if (data[i] == e)
            return i;
    return -1;
}

int count(Element e) {
    for(int i = 0; i < size; i++)
        if (data[i] == e)
            sum += i
            return sum;
    return -1;
}
