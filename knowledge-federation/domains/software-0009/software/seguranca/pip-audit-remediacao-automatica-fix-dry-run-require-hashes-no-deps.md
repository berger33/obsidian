---
id: software.seguranca.tranche16.001583
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
fontes: ["https://raw.githubusercontent.com/pypa/pip-audit/main/README.md", "https://raw.githubusercontent.com/pypa/advisory-database/main/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Correção Automática de Dependências Vulneráveis (**`--fix`** e **`--fix --dry-run`**) e Auditoria Reprodutível com Hashes (**`--require-hashes` / `--no-deps` / `--disable-pip`**) no `pip-audit`

## Em uma frase
Quando o `pip-audit` encontra vulnerabilidades no seu ambiente ou no seu `requirements.txt`, como atualizá-las automaticamente para a menor versão segura (`Fix Version`), e como auditar arquivos `requirements.txt` travados com hashes SHA-256 (`pip-compile --generate-hashes`) **sem sequer invocar o resolvedor do `pip` (`--disable-pip`)**?

## Por que importa
Para correção automática, o `pip-audit` oferece a flag **`--fix`** (e a simulação segura **`--fix --dry-run`**, que executa a auditoria completa e imprime exatamente quais pacotes seriam atualizados sem tocar em nada)!

## Como funciona
E para arquivos `requirements.txt` de alta segurança onde todas as dependências diretas e transitivas já estão fixadas com versão exata (`==`) e hashes `--hash=sha256:...`, você usa **`--require-hashes`** ou **`--no-deps --disable-pip`**: o `pip-audit` lê apenas os nomes, versões e hashes diretamente do arquivo texto e consulta a API de vulnerabilidades em **menos de 1 segundo, sem baixar nem resolver pacotes via `pip`**!

## Exemplo
```bash
# Simular a correcao automatica (--fix --dry-run) e auditar ultra-rapido um requirements.txt travado sem invocar o pip (--no-deps --disable-pip)
pip-audit -r ./requirements.txt --fix --dry-run
pip-audit -r ./requirements-locked.txt --no-deps --disable-pip --strict
```

## Limites e trade-offs
Olhe a segunda linha acima (**`pip-audit -r ./requirements-locked.txt --no-deps --disable-pip --strict`**): além de ser **10x mais rápida** (porque não precisa rodar a resolução de dependências do `pip`), ela é a forma mais segura de auditar código de terceiros não confiável em CI/CD!

## Como verificar
Por quê? Como veremos na próxima nota sobre o *Security Model* do `pip-audit`, quando você audita um `requirements.txt` **sem** versões totalmente pinadas (sem `--no-deps` / `--require-hashes`), o `pip` pode precisar baixar uma distribuição de código-fonte (`.tar.gz` `sdist`) para descobrir as dependências transitivas dela! Com `--no-deps --disable-pip` (ou `--require-hashes` com wheels), **nenhum pacote é baixado nem executado**!

## Conexões
- [[pip-audit-modos-varredura-requirements-pyproject-locked-local-venv]] — Veja também: Auditando Ambientes Virtuais (`-l`), Arquivos `requirements.txt` (`-r`) e Lockfiles de Projetos (`pyproject.toml` / `pylock.*.toml` `--locked`) no `pip-audit`.
- [[pip-audit-modelo-seguranca-resolucao-dependencias-sdist-execucao-codigo]] — Veja também: O Modelo de Segurança do `pip-audit` (**Security Model**): Por Que Auditar `requirements.txt` Não-Pinados Pode Executar `setup.py` e Como Prevenir com `--require-hashes`.
- [[pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv]] — Referência cruzada direta com pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv.

## Fontes
- [PyPA `pip-audit` Official GitHub Repository (`pypa/pip-audit`)](https://raw.githubusercontent.com/pypa/pip-audit/main/README.md) — repositório oficial da ferramenta `pip-audit` da Python Packaging Authority cobrindo flags CLI, variáveis de ambiente, formatos CycloneDX/Markdown/JSON, `--fix` e modelo de segurança; consultado em 2026-10-03.
- [Python Packaging Advisory Database Official Repository (`pypa/advisory-database`)](https://raw.githubusercontent.com/pypa/advisory-database/main/README.md) — repositório oficial de advisories `PYSEC-*` no formato OpenSSF OSV YAML detalhando triagem, validação JSON Schema e marcação de símbolos vulneráveis `ecosystem_specific.imports`; consultado em 2026-10-03.
