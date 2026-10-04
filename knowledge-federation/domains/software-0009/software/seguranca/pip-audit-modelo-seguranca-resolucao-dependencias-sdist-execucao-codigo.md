---
id: software.seguranca.tranche16.001584
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

# O Modelo de Segurança do `pip-audit` (**Security Model**): Por Que Auditar `requirements.txt` Não-Pinados Pode Executar `setup.py` e Como Prevenir com `--require-hashes`

## Em uma frase
Na seção *Security model* do `README.md` oficial do `pip-audit`, os autores da Trail of Bits / PyPA fazem um alerta crucial de segurança que todo engenheiro de AppSec e DevSecOps precisa conhecer: **O que acontece nos bastidores quando você executa `pip-audit -r requirements.txt` sobre um arquivo de requisitos que NÃO tem todas as subdependências pinadas com hashes?**

## Por que importa
Para descobrir quais são as dependências transitivas de um pacote listado no `requirements.txt`, o `pip-audit` precisa resolver a árvore de dependências usando o `pip`. Se um pacote específico no PyPI **não possuir um pacote binário `Wheel` (`.whl`) com metadados `METADATA` estáticos** e só estiver disponível como código-fonte (**`sdist` `.tar.gz`**), o `pip` precisa baixar o `.tar.gz` e **executar o `setup.py` / backend de build do pacote para descobrir suas dependências**!

## Como funciona
Ou seja: auditar um `requirements.txt` vindo de uma fonte não confiável sem `--no-deps` / `--require-hashes` pode executar código arbitrário de `setup.py` durante a resolução!

## Exemplo
```bash
# Gerar um requirements.txt 100% pinado com hashes SHA-256 e audita-lo no pip-audit com --require-hashes e --disable-pip (Zero execucao de codigo!)
pip-audit -r ./requirements-hashed.txt --require-hashes --disable-pip --strict
```

## Limites e trade-offs
Veja como eliminar **100% desse risco** na sua esteira de CI/CD seguindo as recomendações do *Security model* do `pip-audit`: **(1)** Use arquivos de requisitos gerados por `pip-compile --generate-hashes` / `uv pip compile --generate-hashes` / `poetry export --with-hashes`; **(2)** Quando um arquivo já contém `--hash=sha256:...`, o `pip-audit` ativa automaticamente **`--require-hashes`**; e **(3)** Adicione **`--disable-pip`** (ou **`--no-deps --disable-pip`**) para garantir que o `pip-audit` nunca baixe nem construa nenhum `sdist`!

## Como verificar
E se você realmente precisar auditar um `requirements.txt` não-pinado de um repositório externo desconhecido? Execute o `pip-audit` dentro de um container descartável ou sandbox **`bubblewrap` (`bwrap`) / `firejail`** sem acesso aos segredos de produção!

## Conexões
- [[pip-audit-remediacao-automatica-fix-dry-run-require-hashes-no-deps]] — Veja também: Correção Automática de Dependências Vulneráveis (**`--fix`** e **`--fix --dry-run`**) e Auditoria Reprodutível com Hashes (**`--require-hashes` / `--no-deps` / `--disable-pip`**) no `pip-audit`.
- [[pip-audit-geracao-sbom-cyclonedx-json-xml-formatos-markdown-sarif]] — Veja também: Geração Nativa de **SBOM CycloneDX (`-f cyclonedx-json` / `cyclonedx-xml`)**, Relatórios **Markdown (`-f markdown`)** e **JSON** no `pip-audit`.
- [[pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv]] — Referência cruzada direta com pip-audit-arquitetura-pypa-advisory-database-pypi-json-api-osv.

## Fontes
- [PyPA `pip-audit` Official GitHub Repository (`pypa/pip-audit`)](https://raw.githubusercontent.com/pypa/pip-audit/main/README.md) — repositório oficial da ferramenta `pip-audit` da Python Packaging Authority cobrindo flags CLI, variáveis de ambiente, formatos CycloneDX/Markdown/JSON, `--fix` e modelo de segurança; consultado em 2026-10-03.
- [Python Packaging Advisory Database Official Repository (`pypa/advisory-database`)](https://raw.githubusercontent.com/pypa/advisory-database/main/README.md) — repositório oficial de advisories `PYSEC-*` no formato OpenSSF OSV YAML detalhando triagem, validação JSON Schema e marcação de símbolos vulneráveis `ecosystem_specific.imports`; consultado em 2026-10-03.
