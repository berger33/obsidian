---
id: software.seguranca.tranche01.000026
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

# OSV-Scanner License Scanning (`--licenses`): auditoria de licenças de software livre via `deps.dev` e validação contra allowlist SPDX

## Em uma frase
Por meio da flag **`--licenses`**, o OSV-Scanner consulta os metadados do **[deps.dev](https://deps.dev/)** (Google Open Source Insights) para auditar as licenças de todas as dependências diretas e transitivas do projeto e validar se alguma pacote viola a lista de licenças SPDX permitidas pela organização.

## Por que importa
Introduzir inadvertidamente uma biblioteca transitiva sob licença *copyleft* restritiva (como `AGPL-3.0` ou `GPL-3.0-only`) ou sem licença clara (`UNKNOWN`) em um produto comercial distribuído pode gerar risco jurídico e de propriedade intelectual.

## Como funciona
Passar `--licenses` sem argumentos imprime um resumo quantitativo de todas as licenças encontradas; já passar uma lista separada por vírgulas de identificadores SPDX (`--licenses="MIT,Apache-2.0,BSD-3-Clause,ISC"`) faz o scanner falhar e listar exatamente quais pacotes violam a política de conformidade.

## Exemplo
```bash
# Exibindo o resumo de licenças de todas as dependências do repositório:
osv-scanner scan source --licenses ./meu-repositorio

# Validando estritamente contra uma allowlist de identificadores SPDX permitidos:
osv-scanner scan source --licenses="MIT,Apache-2.0,BSD-2-Clause,BSD-3-Clause,ISC" ./meu-repositorio
```

## Limites e trade-offs
Combine `--licenses` com `--offline` caso utilize o banco de dados local baixado previamente em ambientes sem acesso externo ao `deps.dev`.

## Como verificar
Execute `osv-scanner scan source --licenses="MIT,Apache-2.0" .` em seu projeto para verificar se há dependências fora da política.

## Conexões
- [[osvscanner-guided-remediation-fix-in-place-relax-override-pom-npm]] — Veja também: OSV-Scanner Guided Remediation (`osv-scanner fix`): estratégias `in-place`, `relax` e `override` para atualização segura de dependências.
- [[osvscanner-offline-scanning-download-offline-databases-air-gapped]] — Veja também: OSV-Scanner Modo Offline (`--offline-vulnerabilities` e `--download-offline-databases`): operação em redes isoladas e *air-gapped*.

## Fontes
- [Google OSV-Scanner GitHub — README.md (OSV-Scanner V2 Features, OSV-Scalibr Engine, Container Scanning, Call Analysis & Guided Remediation)](https://raw.githubusercontent.com/google/osv-scanner/main/README.md) — README oficial do google/osv-scanner descrevendo a arquitetura V2 baseada no OSV-Scalibr, suporte a lockfiles/SBOMs, imagens de container e remediação guiada; consultado em 2026-10-03.
- [OSV-Scanner Official Documentation — Usage & Configuration (scan source, scan image, fix Strategies, --licenses, Offline DB & osv-scanner.toml)](https://google.github.io/osv-scanner/usage/) — Documentação oficial de uso do OSV-Scanner detalhando flags de CLI, estratégias de osv-scanner fix (in-place, relax, override), auditoria SPDX e osv-scanner.toml; consultado em 2026-10-03.
- [Google OSV-Scanner — Official GitHub Repository](https://github.com/google/osv-scanner) — Repositório oficial Apache-2.0 do Google OSV-Scanner; consultado em 2026-10-03.
