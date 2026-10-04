---
id: software.seguranca.tranche13.001219
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

# Reconstrução de **Atividade de Navegadores e Downloads de Malware (`webhist`)** no Plaso: Chrome/Edge (Chromium), Firefox, Safari e Extensões

## Em uma frase
Em mais de 60% dos incidentes corporativos que começam na estação de um usuário (via *Malvertising*, *Phishing*, *Fake CAPTCHA / ClickFix* ou extensão maliciosa de navegador), a pergunta número 1 da investigação é: **"Qual URL exata o usuário acessou segundos antes de baixar e executar o payload inicial, de onde veio o redirecionamento e quais extensões estavam instaladas no navegador?"**

## Por que importa
O preset **`webhist`** do Plaso reúne parsers especializados para todos os bancos SQLite, caches binários e JSONs dos navegadores modernos: **Google Chrome / Microsoft Edge / Brave / Chromium** (`sqlite/chrome_27_history`, `chrome_66_cookies`, `chrome_autofill`, `chrome_cache`, `chrome_preferences`, `leveldb` de extensões), **Mozilla Firefox** (`sqlite/firefox_history` `places.sqlite`, `firefox_downloads`, `firefox_cookies`, `firefox_cache`) e **Apple Safari** (`safari_history`, `BinaryCookies`)!

## Como funciona
Ao processar o perfil do usuário com `--parsers "webhist,lnk,prefetch,zone_identifier"`, o Plaso alinha na mesma linha do tempo: a busca no buscador -> a cadeia de cliques de redirecionamento HTTP -> o registro de download no `History` SQLite -> a gravação do stream NTFS **`Zone.Identifier` (`HostUrl` / `ReferrerUrl`)** -> a criação do `.lnk` em `Recent` -> e a execução do `.exe`/`.msi` no `Prefetch`!

## Exemplo
```bash
# Extrair exclusivamente a linha do tempo de Navegadores Web, Downloads, Zone.Identifier e Atalhos LNK de uma estacao infectada
log2timeline.py \
  --storage-file ./paciente_zero_webhist.plaso \
  --parsers "webhist,lnk,prefetch,winreg" \
  --unattended \
  ./coleta_kape_estacao01/
```

## Limites e trade-offs
Execute também o plugin de análise **`psort.py --analysis browser_search,chrome_extension`** sobre o arquivo `.plaso` gerado: ele lista automaticamente todas as pesquisas feitas pelo usuário nos mecanismos de busca e inventaria todas as extensões de navegador instaladas por ID da Chrome Web Store!

## Como verificar
Muitas vezes, mesmo que o usuário ou o invasor tenha limpado o histórico do navegador, o artefato NTFS Alternate Data Stream **`Zone.Identifier`** preservado nos arquivos baixados ou as entradas na `$MFT`/`$UsnJrnl` revelam a URL de origem do payload.

## Conexões
- [[plaso-forense-linux-macos-containers-syslog-auditd-plist-unified-logs]] — Veja também: Forense de Servidores **Linux, macOS e Containers** com o Plaso: Parsers `syslog`, `systemd_journal`, `utmp`/`wtmp`, `bash_history`, `fsext` e `plist`.
- [[plaso-otimizacao-performance-workers-memoria-hashes-sha256-escala]] — Veja também: Otimização de Performance e Extração de **Hashes `SHA-256` (`--hashers`)** no `log2timeline.py`: Gerenciando Workers, Memória e Arquivos Grandes.
- [[plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite]] — Referência cruzada direta com plaso-arquitetura-motor-super-timeline-forense-log2timeline-sqlite.
- [[plaso-presets-parsers-customizados-win7-linux-macos-targeted-timelines]] — Referência cruzada direta com plaso-presets-parsers-customizados-win7-linux-macos-targeted-timelines.
- [[gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas]] — Referência cruzada direta com gophish-arquitetura-simulacao-phishing-conscientizacao-campanhas.

## Fontes
- [Plaso (`log2timeline`) Official GitHub — Super Timeline All the Things](https://raw.githubusercontent.com/log2timeline/plaso/main/README.md) — repositório oficial do motor forense Plaso cobrindo arquitetura de parsers, plugins de análise, event tagging e formatos de armazenamento; consultado em 2026-10-03.
- [Plaso Official Documentation — Using `log2timeline.py` (`plaso.readthedocs.io`)](https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html) — documentação oficial do Plaso detalhando extração de imagens E01/RAW, partições, Volume Shadow Copies (`--vss_stores`), BitLocker, presets de parsers e arquitetura multi-worker; consultado em 2026-10-03.
