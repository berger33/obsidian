---
id: software.seguranca.tranche16.001582
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

# Auditando Ambientes Virtuais (`-l`), Arquivos `requirements.txt` (`-r`) e Lockfiles de Projetos (`pyproject.toml` / `pylock.*.toml` `--locked`) no `pip-audit`

## Em uma frase
Qual é a diferença no `pip-audit` entre rodar: **(1) `pip-audit -l`** dentro de um `virtualenv`/container, **(2) `pip-audit -r requirements.txt`** sobre um arquivo de requisitos sem instalar os pacotes, e **(3) `pip-audit --locked .`** na raiz de um projeto Python moderno?

## Por que importa
Veja o comportamento exato de cada modo documentado no `README.md`: **(1) Modo Ambiente Local (`pip-audit -l` / `--local`)** — inspeciona os pacotes instalados no ambiente Python ativo, mas a flag **`-l`** restringe a auditoria apenas aos pacotes instalados localmente no `venv` (ignorando pacotes globais do sistema operacional Linux no `/usr/lib/python3/dist-packages` quando o venv foi criado com `--system-site-packages`!).

## Como funciona
**(2) Modo `requirements.txt` (`pip-audit -r requirements.txt`)** — resolve toda a árvore de dependências transitivas do arquivo `requirements.txt` em um ambiente isolado sem alterar seu sistema; e **(3) Modo Projeto e Lockfiles (`pip-audit .` e `pip-audit --locked .`)** — analisa diretamente o **`pyproject.toml`** e os novos arquivos de lock padronizados **`pylock.*.toml` (`PEP 751`)**!

## Exemplo
```bash
# Auditar multiplos arquivos requirements.txt (-r), um projeto local (pyproject.toml) ou lockfiles padronizados (--locked) com modo estrito (-S)
pip-audit -r ./requirements.txt -r ./requirements-prod.txt --strict
pip-audit --locked .
pip-audit --local --skip-editable
```

## Limites e trade-offs
Por que você deve **SEMPRE adicionar a flag `-S` (`--strict`)** ao executar o `pip-audit` em pipelines de CI/CD? Porque sem `--strict`, se a coleta/resolução de metadados falhar em alguma dependência específica (por exemplo, um pacote com erro de versão ou índice indisponível), o `pip-audit` apenas emite um aviso e continua auditando o restante; já com **`--strict` (`-S`)**, **qualquer falha ao resolver ou inspecionar uma dependência aborta a auditoria imediatamente com erro**, garantindo cobertura de 100%!

## Como verificar
Use também **`--skip-editable`** quando o seu ambiente virtual de desenvolvimento contiver o próprio pacote da sua aplicação instalado em modo editável (`pip install -e .`), pois pacotes locais não publicados no PyPI não existem no índice público.

## Conexões
- [[pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv]] — Veja também: Arquitetura do **`pip-audit` (`pypa/pip-audit`)** e **Python Packaging Advisory Database (`pypa/advisory-database`)**: Serviços **`pypi`** vs. **`osv`** e Reuso do Cache do `pip`.
- [[pip-audit-remediacao-automatica-fix-dry-run-require-hashes-no-deps]] — Veja também: Correção Automática de Dependências Vulneráveis (**`--fix`** e **`--fix --dry-run`**) e Auditoria Reprodutível com Hashes (**`--require-hashes` / `--no-deps` / `--disable-pip`**) no `pip-audit`.
- [[pip-audit-modelo-seguranca-resolucao-dependencias-sdist-execucao-codigo]] — Referência cruzada direta com pip-audit-modelo-seguranca-resolucao-dependencias-sdist-execucao-codigo.

## Fontes
- [PyPA `pip-audit` Official GitHub Repository (`pypa/pip-audit`)](https://raw.githubusercontent.com/pypa/pip-audit/main/README.md) — repositório oficial da ferramenta `pip-audit` da Python Packaging Authority cobrindo flags CLI, variáveis de ambiente, formatos CycloneDX/Markdown/JSON, `--fix` e modelo de segurança; consultado em 2026-10-03.
- [Python Packaging Advisory Database Official Repository (`pypa/advisory-database`)](https://raw.githubusercontent.com/pypa/advisory-database/main/README.md) — repositório oficial de advisories `PYSEC-*` no formato OpenSSF OSV YAML detalhando triagem, validação JSON Schema e marcação de símbolos vulneráveis `ecosystem_specific.imports`; consultado em 2026-10-03.
