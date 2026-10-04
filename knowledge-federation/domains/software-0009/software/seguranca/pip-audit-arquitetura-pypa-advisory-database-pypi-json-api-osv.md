---
id: software.seguranca.tranche16.001581
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

# Arquitetura do **`pip-audit` (`pypa/pip-audit`)** e **Python Packaging Advisory Database (`pypa/advisory-database`)**: Serviços **`pypi`** vs. **`osv`** e Reuso do Cache do `pip`

## Em uma frase
Como o **`pip-audit`** — criado pela **Trail of Bits** com apoio do Google e mantido oficialmente pela **Python Packaging Authority (`PyPA`)** — audita ambientes Python, arquivos `requirements.txt` e projetos `pyproject.toml` em busca de pacotes com vulnerabilidades conhecidas?

## Por que importa
Conforme documentado nos repositórios oficiais `pypa/pip-audit` e `pypa/advisory-database`, o `pip-audit` consulta diretamente a base oficial **`Python Packaging Advisory Database` (`PYSEC-*`)**, onde cada aviso é mantido em YAML seguindo o **OpenSSF OSV Schema (`ossf/osv-schema`)** e enriquecido até o nível de módulos/atributos afetados (`ecosystem_specific.imports`)!

## Como funciona
Por padrão (`-s pypi`), o `pip-audit` consulta o campo `vulnerabilities` da **PyPI JSON API (`warehouse.pypa.io`)** reutilizando de forma transparente o **Cache HTTP Local do próprio `pip`**, ou pode consultar diretamente a API global **`OSV.dev` (`-s osv` / `--osv-url https://api.osv.dev/v1/query`)**!

## Exemplo
```bash
# Auditar o ambiente Python atual com pip-audit exibindo aliases (CVE / GHSA) e descricoes detalhadas de cada vulnerabilidade PYSEC
python3 -m pip_audit --version
pip-audit --aliases --desc
pip-audit -s osv --aliases
```

## Limites e trade-offs
Veja na segunda linha acima as flags **`--aliases`** e **`--desc`**: por padrão na saída em colunas (`-f columns`), o `pip-audit` imprime o identificador primário **`PYSEC-YYYY-NNN`** (ou `GHSA-*`) e a versão corrigida (`Fix Versions`); ao passar `--aliases` e `--desc`, ele exibe na mesma tabela os identificadores **`CVE-YYYY-NNNNN`** e **`GHSA-*`** equivalentes junto com a descrição técnica completa da falha!

## Como verificar
E atenção aos códigos de saída (*Exit Codes*) documentados no `README.md`: **`0`** significa que nenhuma vulnerabilidade foi encontrada, enquanto **`1`** significa que uma ou mais vulnerabilidades foram detectadas (quebrando automaticamente o job de CI/CD)!

## Conexões
- [[pip-audit-modos-varredura-requirements-pyproject-locked-local-venv]] — Veja também: Auditando Ambientes Virtuais (`-l`), Arquivos `requirements.txt` (`-r`) e Lockfiles de Projetos (`pyproject.toml` / `pylock.*.toml` `--locked`) no `pip-audit`.
- [[pip-audit-remediacao-automatica-fix-dry-run-require-hashes-no-deps]] — Referência cruzada direta com pip-audit-remediacao-automatica-fix-dry-run-require-hashes-no-deps.

## Fontes
- [PyPA `pip-audit` Official GitHub Repository (`pypa/pip-audit`)](https://raw.githubusercontent.com/pypa/pip-audit/main/README.md) — repositório oficial da ferramenta `pip-audit` da Python Packaging Authority cobrindo flags CLI, variáveis de ambiente, formatos CycloneDX/Markdown/JSON, `--fix` e modelo de segurança; consultado em 2026-10-03.
- [Python Packaging Advisory Database Official Repository (`pypa/advisory-database`)](https://raw.githubusercontent.com/pypa/advisory-database/main/README.md) — repositório oficial de advisories `PYSEC-*` no formato OpenSSF OSV YAML detalhando triagem, validação JSON Schema e marcação de símbolos vulneráveis `ecosystem_specific.imports`; consultado em 2026-10-03.
