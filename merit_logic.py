import pandas as pd

# 1. تحميل البيانات
df = pd.read_csv('hr_data.csv')

# 2. الفرز الأعمى: إخفاء البيانات غير المتعلقة بالكفاءة (مثل الجنس)
# نحن نحتفظ بالـ ID فقط للتواصل لاحقاً
merit_df = df.drop(columns=['Gender'])

# 3. تحديد أوزان المعايير (يمكنك تعديلها حسب رؤيتك)
# هنا نعطي الاختبار التقني والجاهزية الميدانية الثقل الأكبر
WEIGHT_TECH = 0.40      # 40% للاختبار التقني
WEIGHT_FIELD = 0.30     # 30% للجاهزية الميدانية (الحماية والتدخل)
WEIGHT_LOGIC = 0.20     # 20% للتفكير المنطقي
WEIGHT_PORTFOLIO = 0.10  # 10% لسابقة الأعمال

# 4. حساب "درجة الجدارة النهائية" (Merit Score)
merit_df['Merit_Score'] = (
    (merit_df['Technical_Score'] * WEIGHT_TECH) +
    (merit_df['Field_Readiness'] * WEIGHT_FIELD) +
    (merit_df['Logic_Score'] * WEIGHT_LOGIC) +
    (merit_df['Portfolio_Rating'] * 10 * WEIGHT_PORTFOLIO) # ضربنا في 10 لتوحيد المقياس
)

# 5. ترتيب المرشحين من الأكفأ إلى الأقل كفاءة
top_candidates = merit_df.sort_values(by='Merit_Score', ascending=False)

# 6. عرض أفضل 10 كفاءات ميدانية وتقنية
print("--- قائمة الـ 10 الأوائل بناءً على استحقاق الكفاءة فقط ---")
print(top_candidates[['Candidate_ID', 'Merit_Score', 'Technical_Score', 'Field_Readiness']].head(10))

# 7. حفظ النتائج في ملف جديد للمحفظة
top_candidates.to_csv('merit_results.csv', index=False)
