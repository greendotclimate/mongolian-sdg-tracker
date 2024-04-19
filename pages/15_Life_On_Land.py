import streamlit as st
import streamlit.components.v1 as components

def create_goal_section(number, goal, subdescription, iframe_url):
    st.markdown(f"### {number}. {goal}")
    st.markdown(f"_{subdescription}_")
    components.iframe(iframe_url, height=500)

st.title('Зорилт 15. Хуурай газрын экосистемийг хамгаалах')

st.write('Дэлхийн экосистемийг хамгаалах, нөхөн сэргээх, түүний тогтвортой хэрэглээг дэмжих, ойг тогтвортой ашиглах, цөлжилттэй тэмцэх, хөрсний доройтлыг зогсоох, сэргээх, биологийн олон янз байдал алдагдаж буйг зогсоох')

#JSON table
goals_data = [
    {
        "number": "15.1",
        "goal": "2020 гэхэд олон улсын гэрээний өмнө хүлээсэн үүрэг хариуцлагад нийцүүлэн хуурай газрын болон далайгаас хол цэнгэг усны экосистем, түүний үйлчилгээ, ялангуяа ой, намагшсан газар, уулархаг болон хуурай газрыг хамгаалах, сэргээх, тэдгээрийг тогтвортой ашиглах боломж нөхцөлийг бүрдүүлэх",
        "subgoals": [
            {
                "number": "15.1.1",
                "description": "Ойгоор бүрхэгдсэн газрын нийт газар нутагт эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/forest-area-as-share-of-land-area"
            },
            {
                "number": "15.1.2",
                "description": "Хамгаалалттай газар бүхий хуурай болон цэнгэг усны биологийн олон янз байдлын томоохон газруудын эзлэх хувь, экосистемийн төрлөөр",
                "iframe_url": "https://ourworldindata.org/grapher/terrestrial-protected-areas"
            }
        ]
    },
    {
        "number": "15.2",
        "goal": "2020 он гэхэд бүх төрлийн ойн тогтвортой менежментийг нэвтрүүлэх явдлыг хөхүүлэн дэмжих, цөлжилтийг зогсоох, муудсан ойг сэргээх, ойжуулах, моджуулах ажлыг олон улсын түвшинд [x] хувиар нэмэгдүүлэх",
        "subgoals": [
            {
                "number": "15.2.1",
                "description": "Ойн тогтвортой менежментийн чиглэлээр гарч байгаа ахиц дэвшил",
                "iframe_url": "https://ourworldindata.org/grapher/forest-area-net-change-rate"
            }
        ]
    },
    {
        "number": "15.3",
        "goal": "2020 гэхэд цөлжилттэй тэмцэх, эвдэрч, талхлагдсан газар, хөрс, түүний дотор цөлжилт, ган, үерийн улмаас доройтсон газрыг сэргээх, газрын доройтлыг саармагжуулсан ертөнцийг бий болгохыг эрмэлзэх",
        "subgoals": [
            {
                "number": "15.3.1",
                "description": "Доройтсон газар нутгийн нийт газар нутагт эзлэх хувь",
                "iframe_url": "https://ourworldindata.org/grapher/share-degraded-land"
            }
        ]
    },
    {
        "number": "15.4",
        "goal": "2030 он гэхэд тогтвортой хөгжилд нэн шаардлагатай үр ашгийг бий болгох уулархаг газрын экосистемийн чадавхыг нэмэгдүүлэх зорилгоор уулархаг газрын экосистем, түүний дотор экосистемийн био олон янз байдлыг хамгаалах",
        "subgoals": [
            {
                "number": "15.4.1",
                "description": "Уулын биологийн олон янз байдлын чухал ач холбогдолтой хэсгийг тусгай хамгаалалтад хамруулсан хэмжээ",
                "iframe_url": "https://ourworldindata.org/grapher/coverage-by-protected-areas-of-important-sites-for-mountain-biodiversity"
            },
            {
                "number": "15.4.2",
                "description": "Уулын ногоон хамралтын индекс",
                "iframe_url": "https://ourworldindata.org/grapher/mountain-green-cover-index"
            }
        ]
    },
    {
        "number": "15.5",
        "goal": "Биологийн төрөл зүйлийн амьдардаг газар орны доройтлыг бууруулах, биологийн олон янз байдал алдагдаж буй байдлыг зогсоох, 2020 он гэхэд устах аюулд өртсөн төрөл зүйлийг хамгаалах, урьдчилан сэргийлэх талаар яаралтай, дорвитой арга хэмжээ авах",
        "subgoals": [
            {
                "number": "15.5.1",
                "description": "Улаан дансны индекс",
                "iframe_url": "https://ourworldindata.org/grapher/red-list-index"
            }
        ]
    },
    {
        "number": "15.6",
        "goal": "Генетикийн нөөц баялгийг ашигласнаас хүртэж буй үр ашгийг шударга, тэгш хуваалцах, энэ төрлийн нөөц баялгийг зохистой ашиглах явдлыг дэмжих",
        "subgoals": [
            {
                "number": "15.6.1",
                "description": "Үр өгөөжийг шударга, тэгш хуваарилах нөхцлийг бүрдүүлэх хууль эрх зүй, бодлого, засаг захиргааны тогтолцоотой эсэх",
                "iframe_url": "https://ourworldindata.org/grapher/countries-to-access-and-benefit-sharing-clearing-house"
            }
        ]
    },
    {
        "number": "15.7",
        "goal": "Ургамлын болон амьтны аймгийн хамгаалагдсан төрөл зүйлийг хулгайгаар агнах, хууль бусаар наймаалах явдлыг зогсоох, зэрлэг амьтан, ургамлын хууль бус бүтээгдэхүүнүүдийг эрэлт, нийлүүлэлтийг шийдэх чиглэлээр яаралтай арга хэмжээ авах",
        "subgoals": [
            {
                "number": "15.7.1",
                "description": "Хулгайгаар, хууль бусаар агнасан зэрлэг ан амьтдыг арилжсан худалдааны эзлэх хувь"
            }
        ]
    },
    {
        "number": "15.8",
        "goal": "2020 он гэхэд өөр гарагийн үржимхий төрөл зүйлийг нутагшуулахаас сэргийлэх, тэдгээрийн хуурай газар болон усны экосистемд нөлөөлж буй нөлөөллийг үлэмж хэмжээгээр бууруулах, зонхилж буй төрөл зүйлийг хянах, устгах арга хэмжээ авах",
        "subgoals": [
            {
                "number": "15.8.1",
                "description": "Харийн төрөл зүйлийг тархахаас сэргийлэх, хяналт тавих ажлыг хангалттай санхүүжүүлдэг, холбогдох хууль эрх зүйн орчин бүрдсэн эсэх",
                "iframe_url": "https://ourworldindata.org/grapher/budget-to-manage-invasive-alien-species"
            }
        ]
    },
    {
        "number": "15.9",
        "goal": "2020 он гэхэд экосистем, биологийн олон янз байдлын ач холбогдлыг үндэсний болон орон нутгийн төлөвлөлт, хөгжлийн бодлого боловсруулалт, ядуурлыг бууруулах стратегид тусгах",
        "subgoals": [
            {
                "number": "15.9.1",
                "description": "Биологийн төрөл зүйлийн 2011-2020 стратегийн төлөвлөгөөний Айчи Биологийн олон янз байдлын Зорилт 2-т заасны дагуу тогтоосон үндэсний зорилтод чиглэсэн ахиц дэвшил",
                "iframe_url": "https://ourworldindata.org/grapher/countries-using-the-system-of-environmental-economic-accounting"
            }
        ]
    },
    {
        "number": "15.a",
        "goal": "Биологийн олон янз байдал, экосистемийг хамгаалах, тогтвортой ашиглах үүднээс бүх төрлийн эх үүсвэрээс санхүү хөрөнгө бүрдүүлэх, түүний хэмжээг нь ихээхэн нэмэгдүүлэх",
        "subgoals": [
            {
                "number": "15.a.1",
                "description": "Биологийн олон янз байдал, экосистемийг тогтвортой ашиглах, хамгаалахад чиглэсэн албан ёсны хөгжлийн тусламж болон засгийн газрын төсвийн зарлагын хэмжээ",
                "iframe_url": "https://ourworldindata.org/grapher/total-oda-for-biodiversity-by-recipient"
            }
        ]
    },
    {
        "number": "15.b",
        "goal": " Тогтвортой ойн менежментийг санхүүжүүлэх зорилгоор бүх түвшинд, бүх төрлийн эх үүсвэрээс ихээхэн хэмжээний хөрөнгө мөнгө бүрдүүлэх, энэ төрлийн менежмент, түүний дотор ойг хамгаалах, ойжуулах менежментийг хөгжүүлэх үүднээс хөгжиж буй орнуудад түлхэц болохуйц урамшуулал олгох",
        "subgoals": [
            {
                "number": "15.b.1",
                "description": "Биологийн олон янз байдал, экосистемийг тогтвортой ашиглах, хамгаалахад чиглэсэн албан ёсны хөгжлийн тусламж болон засгийн газрын төсвийн зарлагын хэмжээ",
                "iframe_url": "https://ourworldindata.org/grapher/total-oda-for-biodiversity-by-recipient"
            }
        ]
    },
    {
        "number": "15.c",
        "goal": "Тогтвортой амьжиргааны нөөц боломжийг бүрдүүлэх зорилгоор орон нутгийн чадавхыг нэмэгдүүлэх замаар хамгаалагдсан төрөл зүйлийг хууль бусаар агнах, арилжих ажиллагаатай тэмцэх хүчин чармайлтыг дэмжсэн олон улсын туслалцаа дэмжлэгийг нэмэгдүүлэх",
        "subgoals": [
            {
                "number": "15.c.1",
                "description": "Хулгайгаар, хууль бусаар агнасан зэрлэг ан амьтдыг арилжсан худалдааны эзлэх хувь"
            }
        ]
    }
]

 

def create_goal_section(number, goal, subgoals):
    st.markdown(f"### {number}. {goal}")
    for subgoal in subgoals:
        st.markdown(f"_{subgoal['number']}. {subgoal['description']}_")
        if 'iframe_url' in subgoal:
            components.iframe(subgoal['iframe_url'], height=500)
        else:
            st.markdown("Мэдээлэл байхгүй байна.")

for data in goals_data:
    create_goal_section(
        number=data["number"],
        goal=data["goal"],
        subgoals=data["subgoals"]
    )
st.divider()

st.markdown("<p style='text-align: center; color: black;'>All plots generated by Our World In Data are under CC-BY License of Fair Use.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black;'>2024 © Green Dot Climate</p>", unsafe_allow_html=True)