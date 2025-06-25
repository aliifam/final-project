return jsonify({
    "current_snapshot": current_snapshot_data,
    "future_forecast": {"actual_start_date": query_forecast_start_date.isoformat(), "actual_end_date": query_forecast_end_date.isoformat(), "daily_utilization": future_forecast_data_list},
    "historical_utilization_trend": {"actual_start_date": query_historical_start_date.isoformat(), "actual_end_date": query_historical_end_date.isoformat(), "daily_utilization": historical_utilization_list}
}), 200