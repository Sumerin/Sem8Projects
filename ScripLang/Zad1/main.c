#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define INF 50000
#define M_INF -INF

#define BATCH_SIZE 3000
char *Data[BATCH_SIZE][5];

int len(const char *src) {
    int length = 0;
    while (*(src++) != 0) {
        length++;
    }
    return length;
}

int count(const char *src, const char *substring, int start, int end) {
    int count = 0;
    int src_itr = 0;
    int c_src_itr = 0;
    int substring_itr = 0;
    int result = 0;
    int src_len = len(src);
    int substring_len = len(substring);

    if (start != M_INF && start > (-src_len)) {
        if (src_len > 0 && start < 0) {
            start = start + src_len;
        }
        src_itr = start;
    }

    if (end != INF && end < src_len) {
        if (end <= -src_len) {
            end = 0;
        } else if (src_len > 0 && end < 0 && end > (-src_len)) {
            end = end + src_len;
        }
        src_len = end;
    }

    if (substring_len == 0) {
        int result = src_len + 1 - src_itr;
        if (result < 0) {
            result = 0;
        }
        return result;
    }

    while (src_itr < src_len) {
        if (src[src_itr] == substring[0]) {
            c_src_itr = src_itr;
            substring_itr = 0;

            while (substring_itr < substring_len && c_src_itr < src_len && src[c_src_itr] == substring[substring_itr]) {
                c_src_itr += 1;
                substring_itr += 1;
            }

            if (substring_itr == substring_len) {
                count += 1;
                src_itr = c_src_itr - 1;
            }
        }
        src_itr += 1;
    }
    return count;
}


void Test1() {
    int result = count("eeeea", "e", M_INF, INF);

    printf("Test 1: %d\n", result == 4);
}

void Test2() {
    int result = count("eeee", "eeee", M_INF, INF);

    printf("Test 2: %d\n", result == 1);
}

void Test3() {
    int result = count("eeadx", "ead", M_INF, INF);

    printf("Test 3: %d\n", result == 1);
}

void Test4() {
    int result = count("eeadx", "sad", M_INF, INF);

    printf("Test 4: %d\n", result == 0);
}

void Test5() {
    int result = count("ee", "eee", M_INF, INF);

    printf("Test 5: %d\n", result == 0);
}

void Test6() {
    int result = count("eaeae", "eae", M_INF, INF);

    printf("Test 6: %d\n", result == 1);
}

void Test7() {
    int result = count("eee", "ee", M_INF, INF);

    printf("Test 7: %d\n", result == 1);
}

void Test8() {
    int result = count("eee", "", M_INF, INF);

    printf("Test 8: %d\n", result == 4);
}

void Test9() {
    int result = count("", "", M_INF, INF);

    printf("Test 9: %d\n", result == 1);
}

void Test10() {
    int result = count("", "ea", M_INF, INF);

    printf("Test 10: %d\n", result == 0);
}

void TestOptional_1() {
    int result = count("eeee", "ee", 1, INF);
    printf("TestOptional 1: %d\n", result == 1);

}

void TestOptional_2() {
    int result = count("eeee", "ee", M_INF, 2);
    printf("TestOptional 2: %d\n", result == 1);

}

void TestOptional_3() {
    int result = count("eeee", "ee", 1, 3);
    printf("TestOptional 3: %d\n", result == 1);

}

void TestOptional_4() {
    int result = count("eeee", "ee", 2, 2);
    printf("TestOptional 4: %d\n", result == 0);

}

void TestOptional_5() {
    int result = count("eeee", "ee", 3, 1);
    printf("TestOptional 5: %d\n", result == 0);

}

void TestOptional_6() {
    int result = count("eeee", "", 1, 2);
    printf("TestOptional 6: %d\n", result == 2);

}

void TestOptional_7() {
    int result = count("eeee", "", 3, 1);
    printf("TestOptional 7: %d\n", result == 0);

}

void TestOptional_8() {
    int result = count("", "e", 3, 1);
    printf("TestOptional 8: %d\n", result == 0);

}

void TestOptional_9() {
    int result = count("", "", 1, 0);
    printf("TestOptional 9: %d\n", result == 0);

}

void TestOptional_10() {
    int result = count("", "", 0, 0);
    printf("TestOptional 10: %d\n", result == 1);

}

void TestOptional_11() {
    int result = count("eee", "e", M_INF, 5);
    printf("TestOptional 11: %d\n", result == 3);

}

void TestOptional_12() {
    int result = count("eee", "e", 3, INF);
    printf("TestOptional 12: %d\n", result == 0);

}

void TestOptional_13() {
    int result = count("eee", "e", -1, INF);
    printf("TestOptional 13: %d\n", result == 1);

}

void TestOptional_14() {
    int result = count("eee", "e", M_INF, -1);
    printf("TestOptional 14: %d\n", result == 2);

}

void TestOptional_15() {
    int result = count("eee", "e", -4, INF);
    printf("TestOptional 15: %d\n", result == 3);

}

void TestOptional_16() {
    int result = count("eee", "e", M_INF, -4);
    printf("TestOptional 16: %d\n", result == 0);

}

void TestOptional_17() {
    int result = count("eee", "e", 5, INF);
    printf("TestOptional 17: %d\n", result == 0);

}

void TestOptional_18() {
    int result = count("eee", "e", -4, 4);
    printf("TestOptional 18: %d\n", result == 3);

}

void TestOptional_19() {
    int result = count("eee", "e", 4, -4);
    printf("TestOptional 19: %d\n", result == 0);

}

void TestOptional_20() {
    int result = count("", "", -2, 2);
    printf("TestOptional 20: %d\n", result == 1);
}

void TestOptional_21() {
    int result = count("UopIcFIdtQFYjODqeukuPvSxT", "", -639, -607);
    printf("TestOptional 21: %d\n", result == 1);
}

void UnitTest() {
    Test1();
    Test2();
    Test3();
    Test4();
    Test5();
    Test6();
    Test7();
    Test8();
    Test9();
    Test10();
    TestOptional_1();
    TestOptional_2();
    TestOptional_3();
    TestOptional_4();
    TestOptional_5();
    TestOptional_6();
    TestOptional_7();
    TestOptional_8();
    TestOptional_9();
    TestOptional_10();
    TestOptional_11();
    TestOptional_12();
    TestOptional_13();
    TestOptional_14();
    TestOptional_15();
    TestOptional_16();
    TestOptional_17();
    TestOptional_18();
    TestOptional_19();
    TestOptional_20();
}

void LoadData() {
    FILE *file;
    char *line = NULL;
    size_t len = 0;
    int itr = 0;
    int i = 0;
    ssize_t read;

    file = fopen("Test_data", "r");
    if (file == NULL) {
        printf("failed to open file");
        return;
    }

    while ((read = getline(&line, &len, file)) != -1) {


        //printf("Line: %s",line);
        for (i = 0; i < 5; i++) {

            Data[itr][i] = line;
            while (*line != ';' && *line != '\n' && *line != '\0') {
                line++;
            }
            if (*line == '\n') {
                *line = '\0';
                break;
            }
            *line = '\0';
            //printf("t: %s\n",Data[itr][i]);
            line++;
        }
        //printf("%s %s %s %s %s\n",Data[itr][0],Data[itr][1],Data[itr][2],Data[itr][3],Data[itr][4]);
        itr++;
        line = NULL;
    }

    printf("Loaded\n");
    fclose(file);
}

void CheckMyCountFunction() {
    FILE *file;
    int i = 0;
    int result = 0;
    int myresult = 0;
    int start = 0;
    int end = 0;
    const char *subString = NULL;
    const char *src = NULL;

    file = fopen("Test_error", "w");
    if (file == NULL) {
        printf("failed to open error file");
        return;
    }

    for (i = 0; i < BATCH_SIZE; ++i) {
        result = atoi(Data[i][0]);
        start = atoi(Data[i][1]);
        end = atoi(Data[i][2]);
        subString = Data[i][3];
        src = Data[i][4];

        myresult = count(src, subString, start, end);

        if (myresult != result) {
            printf("Error\n");
            myresult = count(src, subString, start, end);
            fprintf(file, "%d;%d;%d;%d;%s;%s\n", result, myresult, start, end, subString, src);
        }
    }
    printf("Checked\n");
    fclose(file);
}

void TimeTest()
{
    int t = 0;
    int i = 0;
    int j = 0;
	int p=0;
    clock_t before;
    clock_t after;
    double loopTime;
    double myImplTime;
    int result = 0;
    int myresult = 0;
    int start = 0;
    int end = 0;
    const char *subString = NULL;
    const char *src = NULL;
	FILE *file;

    
    file = fopen("resultC", "w");
for(p=0 ;p<4;p++)
{
    before = clock();
    for (i = 0; i < BATCH_SIZE; ++i) {
        start = atoi(Data[i][1]);
        end = atoi(Data[i][2]);
        subString = Data[i][3];
        src = Data[i][4];
        for (j=0;j<1000;j++)
        {
            t+=1;
        }
    }
    after = clock();

    loopTime = (after - before)*1.0 /CLOCKS_PER_SEC;

    before = clock();
    for (i = 0; i < BATCH_SIZE; ++i) {
        start = atoi(Data[i][1]);
        end = atoi(Data[i][2]);
        subString = Data[i][3];
        src = Data[i][4];
        for (j=0;j<1000;j++)
        {
            t+=1;
            count(src,subString,start,end);
        }
    }
    after = clock();

    myImplTime = ((after - before)*1.0 /CLOCKS_PER_SEC);

    printf("LoopTime: %f MyImplTime: %f\n",loopTime, myImplTime);
	fprintf(file, "%f;%f\n", myImplTime, loopTime);
}
}


int main() {

    //UnitTest();

    printf("%ld\n %lu", CLOCKS_PER_SEC, sizeof(void*)*8);

    LoadData();
    //CheckMyCountFunction();//Uncomment for checking result with pyton native function.
    TimeTest();

    return 0;
}
