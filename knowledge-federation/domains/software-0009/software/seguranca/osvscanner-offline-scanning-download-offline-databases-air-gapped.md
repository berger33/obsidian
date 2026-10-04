---
id: software.seguranca.tranche01.000027
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/google/osv-scanner/main/README.md", "https://google.github.io/osv-scanner/usage/", "https://github.com/google/osv-scanner"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OSV-Scanner Modo Offline (`--offline-vulnerabilities` e `--download-offline-databases`): operação em redes isoladas e *air-gapped*

## Em uma frase
Para ambientes de build isolados da internet (*air-gapped*), runners de CI sem acesso externo ou equipes que exigem privacidade total da lista de pacotes, o OSV-Scanner oferece as flags **`--offline-vulnerabilities`** (ou `--offline`) e **`--download-offline-databases`**.

## Por que importa
Na operação online padrão, o OSV-Scanner envia os nomes e versões dos pacotes extraídos para a API do `osv.dev`; em redes industriais/governamentais sem internet ou projetos confidenciais, nenhuma chamada externa pode sair do runner.

## Como funciona
Em uma máquina conectada (ou job de atualização de cache), você executa `osv-scanner --offline-vulnerabilities --download-offline-databases` para baixar os arquivos `.zip` do banco OSV por ecossistema para o diretório local (`OSV_SCANNER_LOCAL_DB_CACHE_DIRECTORY`), e depois executa `osv-scanner --offline-vulnerabilities` nos runners desconectados.

## Exemplo
```bash
# 1. Pré-aquecendo o cache local de bancos de vulnerabilidades OSV em diretório dedicado:
export OSV_SCANNER_LOCAL_DB_CACHE_DIRECTORY=/var/cache/osv-db
osv-scanner scan source --offline-vulnerabilities --download-offline-databases .

# 2. Executando varredura 100% offline sem realizar chamadas de rede:
osv-scanner scan source --offline-vulnerabilities .
```

## Limites e trade-offs
Atualize periodicamente o volume em `OSV_SCANNER_LOCAL_DB_CACHE_DIRECTORY` (por exemplo via CronJob diário) para garantir que CVEs recém-publicadas estejam presentes nas varreduras offline.

## Como verificar
Teste a execução desconectada passando `--offline-vulnerabilities` e confirmando que nenhuma requisição externa é necessária após o download.

## Conexões
- [[osvscanner-license-scanning-deps-dev-spdx-allowlist-compliance]] — Veja também: OSV-Scanner License Scanning (`--licenses`): auditoria de licenças de software livre via `deps.dev` e validação contra allowlist SPDX.
- [[osvscanner-configuracao-osv-scanner-toml-ignoredvulns-packageoverrides]] — Veja também: OSV-Scanner `osv-scanner.toml`: supressão auditável (`IgnoredVulns` com `ignoreUntil`) e sobrescrita (`PackageOverrides`).

## Fontes
- [Google OSV-Scanner GitHub — README.md (OSV-Scanner V2 Features, OSV-Scalibr Engine, Container Scanning, Call Analysis & Guided Remediation)](https://raw.githubusercontent.com/google/osv-scanner/main/README.md) — README oficial do google/osv-scanner descrevendo a arquitetura V2 baseada no OSV-Scalibr, suporte a lockfiles/SBOMs, imagens de container e remediação guiada; consultado em 2026-10-03.
- [OSV-Scanner Official Documentation — Usage & Configuration (scan source, scan image, fix Strategies, --licenses, Offline DB & osv-scanner.toml)](https://google.github.io/osv-scanner/usage/) — Documentação oficial de uso do OSV-Scanner detalhando flags de CLI, estratégias de osv-scanner fix (in-place, relax, override), auditoria SPDX e osv-scanner.toml; consultado em 2026-10-03.
- [Google OSV-Scanner — Official GitHub Repository](https://github.com/google/osv-scanner) — Repositório oficial Apache-2.0 do Google OSV-Scanner; consultado em 2026-10-03.
