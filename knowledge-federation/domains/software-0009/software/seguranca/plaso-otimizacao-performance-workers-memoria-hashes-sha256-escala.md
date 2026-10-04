---
id: software.seguranca.tranche13.001220
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/log2timeline/plaso/main/README.md", "https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Otimização de Performance e Extração de **Hashes `SHA-256` (`--hashers`)** no `log2timeline.py`: Gerenciando Workers, Memória e Arquivos Grandes

## Em uma frase
Ao processar imagens de disco grandes com o `log2timeline.py`, dois parâmetros determinam diretamente a velocidade da extração e a riqueza forense dos eventos de arquivos: a configuração de **Hashers (`--hashers`)** e o gerenciamento de **Processos Workers (`--workers` e `--buffer_size`)**!

## Por que importa
Por padrão, o `log2timeline.py` calcula o hash **`sha256`** (controlado por `--hashers sha256` ou `--hashers md5,sha1,sha256` ou `--hashers none`) para os arquivos processados pelo parser `filestat` (com tamanho até `--hasher_file_size_limit`), anexando o `sha256_hash` diretamente aos eventos de sistema de arquivos da Super Timeline!

## Como funciona
Em máquinas de análise forense com muitos núcleos de CPU e SSD NVMe rápido, se você quiser gerar uma Super Timeline estrutural ultrarrápida sem ler cada byte de grandes arquivos de mídia/bancos de dados para calcular hash, passar **`--hashers none`** (ou limitar `--hasher_file_size_limit 10485760` para 10 MB) reduz o tempo de processamento de horas para minutos!

## Exemplo
```bash
# Executar log2timeline.py ajustando o numero de workers, calculando apenas SHA-256 para executaveis/arquivos ate 20 MB e gravando log de diagnostico
log2timeline.py \
  --storage-file ./servidor_rapido.plaso \
  --workers 8 \
  --hashers sha256 \
  --hasher_file_size_limit 20971520 \
  --logfile ./log2timeline_exec.log.gz \
  --unattended \
  ./evidencias/servidor_app.E01
```

## Limites e trade-offs
Monitore a janela de status do `log2timeline.py` durante a execução: se um `Worker_XX` ficar preso por muito tempo em um único arquivo gigante (como `pagefile.sys`, `hiberfil.sys` ou um banco SQL `.mdf` de 100 GB), lembre-se de que arquivos de memória bruta (`hiberfil.sys` / `MEMORY.DMP`) devem ser analisados com o **Volatility 3** e não por parsers de texto do Plaso!

## Como verificar
Grave sempre o arquivo de saída `.plaso` em um disco **SSD NVMe local rápido** (e nunca em um compartilhamento de rede SMB/NFS lento), pois o processo de *Storage* do Plaso realiza milhares de transações SQLite por segundo ao mesclar as filas dos workers.

## Conexões
- [[plaso-forense-navegadores-webhist-chrome-firefox-edge-downloads-cookies]] — Veja também: Reconstrução de **Atividade de Navegadores e Downloads de Malware (`webhist`)** no Plaso: Chrome/Edge (Chromium), Firefox, Safari e Extensões.
- [[plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite]] — Referência cruzada direta com plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite.
- [[plaso-extracao-imagens-disco-log2timeline-particoes-vss-bitlocker]] — Referência cruzada direta com plaso-extracao-imagens-disco-log2timeline-particoes-vss-bitlocker.
- [[chainsaw-workflow-integrado-chainsaw-hayabusa-kape-velociraptor-dfir]] — Referência cruzada direta com chainsaw-workflow-integrado-chainsaw-hayabusa-kape-velociraptor-dfir.

## Fontes
- [Plaso (`log2timeline`) Official GitHub — Super Timeline All the Things](https://raw.githubusercontent.com/log2timeline/plaso/main/README.md) — repositório oficial do motor forense Plaso cobrindo arquitetura de parsers, plugins de análise, event tagging e formatos de armazenamento; consultado em 2026-10-03.
- [Plaso Official Documentation — Using `log2timeline.py` (`plaso.readthedocs.io`)](https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html) — documentação oficial do Plaso detalhando extração de imagens E01/RAW, partições, Volume Shadow Copies (`--vss_stores`), BitLocker, presets de parsers e arquitetura multi-worker; consultado em 2026-10-03.
