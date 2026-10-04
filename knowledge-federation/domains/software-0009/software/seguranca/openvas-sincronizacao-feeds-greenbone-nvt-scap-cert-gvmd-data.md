---
id: software.seguranca.tranche16.001502
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md", "https://raw.githubusercontent.com/greenbone/gvmd/main/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Sincronização dos Feeds de Inteligência do Greenbone (**`greenbone-feed-sync`**): **NVTs (NASL)**, **SCAP (`CVE` / `CPE`)**, **CERT (`DFN-CERT`)** e **`GVMD_DATA`**

## Em uma frase
Por que uma instalação recém-subida do Greenbone / OpenVAS não deve iniciar nenhuma varredura antes que os **4 Feeds de Inteligência do Greenbone Community Feed** estejam 100% sincronizados e processados pelo `gvmd` e pelo `openvas-scanner`?

## Por que importa
Porque o motor `openvas-scanner` e o `gvmd` dependem de quatro bases complementares atualizadas diariamente: **(1) Feed `NVT` (*Network Vulnerability Tests*)** — mais de 100.000 scripts `.nasl` e advisories Notus carregados pelo `openvas-scanner` no Redis; **(2) Feed `SCAP`** — dicionário oficial de **CPEs e CVEs** consumido pelo `gvmd` para correlação e *CVE Scan*; **(3) Feed `CERT`** — boletins `DFN-CERT` e `CERT-Bund`; e **(4) Feed `GVMD_DATA`** — configurações padrão de Scan Configs (*Full and fast*), Port Lists, Report Formats (PDF, XML, CSV) e Compliance Policies!

## Como funciona
Na arquitetura moderna do GVM 22.4+, todas as sincronizações foram unificadas na ferramenta **`greenbone-feed-sync`** (ou nos containers de dados `vulnerability-tests`, `scap-data`, `cert-data` e `dfn-cert-data`)!

## Exemplo
```bash
# Sincronizar todos os feeds da Greenbone Community Edition (NVT, SCAP, CERT e GVMD_DATA) e verificar o status de carregamento no gvmd
greenbone-feed-sync --type all
gvmd --get-scanners
```

## Limites e trade-offs
Preste atenção a um detalhe operacional clássico após rodar o `greenbone-feed-sync` pela primeira vez: mesmo depois que o `rsync` termina de baixar os arquivos XML/NASL do feed para `/var/lib/gvm/` e `/var/lib/openvas/plugins/`, o daemon **`gvmd` leva alguns minutos em background processando e indexando os milhares de CVEs e CPEs no banco PostgreSQL**! Se você tentar criar uma Task antes de o `gvmd` concluir a importação do `GVMD_DATA`, a lista de *Scan Configs* (`Full and fast`) aparecerá vazia!

## Como verificar
Verifique sempre na aba *Administration -> Feed Status* da interface GSA (ou nos logs `/var/log/gvm/gvmd.log`) que o status dos 4 feeds mudou de *Update in progress...* para **`Current`** antes de disparar varreduras.

## Conexões
- [[openvas-arquitetura-greenbone-gvm-gvmd-ospd-openvas-notus-gsa]] — Veja também: Arquitetura do **Greenbone Vulnerability Management (GVM / OpenVAS)**: **`gvmd` (`GMP`)**, **`ospd-openvas` (`OSP`)**, **`openvas-scanner`**, **`notus-scanner`** e PostgreSQL/Redis.
- [[openvas-configuracao-alvos-targets-port-lists-alive-test-credenciais]] — Veja também: Configuração de **Targets, Port Lists e `Alive Test`** no Greenbone/OpenVAS: Evitando Falsos Negativos em Hosts com Firewall que Bloqueia `ICMP Echo`.
- [[openscap-varredura-vulnerabilidades-cve-oval-eval-security-feeds]] — Referência cruzada direta com openscap-varredura-vulnerabilidades-cve-oval-eval-security-feeds.

## Fontes
- [Greenbone OpenVAS Scanner Official GitHub Repository (`greenbone/openvas-scanner`)](https://raw.githubusercontent.com/greenbone/openvas-scanner/main/README.md) — repositório oficial do motor de varredura OpenVAS e implementação Rust `openvasd` da Greenbone Community Edition; consultado em 2026-10-03.
- [Greenbone Vulnerability Manager (`gvmd`) Official Repository (`greenbone/gvmd`)](https://raw.githubusercontent.com/greenbone/gvmd/main/README.md) — documentação oficial do serviço central `gvmd` cobrindo protocolos GMP e OSP, autenticação JWT, exportação de inteligência e `cve_scan_matching_version`; consultado em 2026-10-03.
