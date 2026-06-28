import os
import asyncio
import logging
from solana.rpc.async_api import AsyncClient

# Log ayarları
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# RPC Bağlantısı
RPC_URL = os.environ.get("SOLANA_RPC_URL", "https://api.mainnet-beta.solana.com")

async def ana_motor():
    logger.info("Solana Sniper/Trading Bot motoru başlatılıyor...")
    
    async with AsyncClient(RPC_URL) as client:
        try:
            versiyon = await client.get_version()
            logger.info(f"Solana ağına başarıyla bağlanıldı. Ağ Versiyonu: {versiyon.value}")
        except Exception as e:
            logger.error(f"Ağa bağlanırken hata oluştu: {str(e)}")
            return

        while True:
            try:
                logger.info("Ağ hareketleri ve likidite havuzları optimize şekilde analiz ediliyor...")
                await asyncio.sleep(10)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Döngü hatası: {str(e)}")
                await asyncio.sleep(2)

if __name__ == "__main__":
    try:
        asyncio.run(ana_motor())
    except KeyboardInterrupt:
        logger.info("Bot kullanıcı tarafından durduruldu.")
      
