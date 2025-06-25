return jsonify({
    "hotel_name": hotel_info.name,
    "stats_kpi": stats_kpi_data,
    "financial_trend_chart": financial_trend_chart_data,
    "best_selling_pods_by_revenue": best_pods_by_revenue_data,
    "top_pods_by_sold": top_pods_by_sold_data,
    "monthly_booking_growth": monthly_booking_growth_data,
    "payment_method_trends": payment_method_line_chart_data,
    "busiest_booking_days": busiest_booking_days_data,
    "recent_activity": recent_activity_data,
    "top_booking_durations": top_booking_durations_data,
    "top_expenses_category": top_expenses_category_data,
})