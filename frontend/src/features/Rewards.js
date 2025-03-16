import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Rewards = () => {
  const [rewards, setRewards] = useState([]);
  const [points, setPoints] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setError('');

      try {
        const rewardsResponse = await axios.get('http://localhost:5000/api/rewards');
        setRewards(rewardsResponse.data);

        const pointsResponse = await axios.get('http://localhost:5000/api/user_points');
        setPoints(pointsResponse.data.points);
      } catch (error) {
        console.error('Error fetching data:', error);
        setError('حدث خطأ أثناء جلب البيانات. الرجاء المحاولة مرة أخرى.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const handleRedeem = async (rewardId) => {
    setLoading(true);
    setError('');

    try {
      await axios.post('http://localhost:5000/api/redeem_reward', { reward_id: rewardId });
      alert('تم استبدال المكافأة بنجاح!');
    } catch (error) {
      console.error('Error redeeming reward:', error);
      setError('فشل في استبدال المكافأة. الرجاء المحاولة مرة أخرى.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <h2 className="text-xl font-bold mb-4">نقاطك: {points}</h2>
      {error && <p className="text-red-500 mb-4">{error}</p>}
      {loading ? (
        <p>جاري التحميل...</p>
      ) : (
        <ul>
          {rewards.map((reward, index) => (
            <li key={index} className="p-2 border-b">
              <div className="flex justify-between items-center">
                <span>
                  {reward[2]} - {reward[3]} نقاط
                </span>
                <button
                  onClick={() => handleRedeem(reward[0])}
                  disabled={loading}
                  className={`bg-green-500 text-white p-2 rounded ${
                    loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-green-500 text-white'
                  }`}
                >
                  استبدال
                </button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Rewards;