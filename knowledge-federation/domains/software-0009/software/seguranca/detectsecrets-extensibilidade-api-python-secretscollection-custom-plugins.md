---
id: software.seguranca.tranche11.001066
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md", "https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# API Python do `detect-secrets` (**`SecretsCollection` & `transient_settings`**): Criando **Plugins e Filtros Customizados (`file://...`)**

## Em uma frase
Um dos recursos mais poderosos do `detect-secrets` (demonstrado no `README.md` oficial) é que ele foi desenhado como uma **Biblioteca Python de Primeira Classe (`from detect_secrets import SecretsCollection`)** e aceita carregar **Plugins Detectores Customizados** e **Filtros Customizados (inclusive modelos de Machine Learning / LLMs locais!)** diretamente via URI **`file://caminho/script.py`**!

## Por que importa
Como criar um **Plugin Detector Customizado** para o formato interno de tokens da sua empresa? Basta criar uma classe Python herdando de `RegexBasedDetector` definindo `secret_type = "Token Interno Corp"` e `denylist = [re.compile(r"CORP_[A-Za-z0-9]{40}")]`, e passá-la com **`-p file:///caminho/meu_plugin.py`**!

## Como funciona
E como criar um **Filtro Customizado**? Basta escrever uma função Python `def meu_filtro(filename: str, line: str, secret: str) -> bool:` (que retorna `True` se o achado deve ser ignorado/filtrado ou `False` se deve ser mantido) e registrá-la com **`-f file://caminho/filtro.py::meu_filtro`**!

## Exemplo
```python
import json
from detect_secrets import SecretsCollection
from detect_secrets.settings import transient_settings

# Usar a API Python do detect-secrets (SecretsCollection + transient_settings) para varrer arquivos programaticamente
secrets = SecretsCollection()
with transient_settings(
    {
        "plugins_used": [
            {"name": "AWSKeyDetector"},
            {"name": "PrivateKeyDetector"},
            {"name": "Base64HighEntropyString", "limit": 4.8},
        ]
    }
):
    secrets.scan_file("README.md")

print(json.dumps(secrets.json(), indent=2))
```

## Limites e trade-offs
Por que a arquitetura de filtros via `file://caminho/filtro.py::minha_funcao` é tão flexível? Porque os parâmetros da função de filtro no `detect-secrets` são injetados dinamicamente por *Dependency Injection* baseada no nome dos argumentos (`filename`, `line`, `secret`, `line_num`, `context`, `plugin`), permitindo que seu filtro inspecione até as linhas vizinhas (`context`) para decidir se é um segredo real!

## Como verificar
Ao usar a API `SecretsCollection`, você pode embutir o motor do `detect-secrets` dentro de robôs de auditoria de logs, tickets do Jira, mensagens do Slack ou dumps de funções AWS Lambda.

## Conexões
- [[detectsecrets-sistema-filtros-heuristicos-custom-filters-allowlist]] — Veja também: Arquitetura de **Filtros Heurísticos (`filters_used`)**, Dicionários (**`--word-list`**), Exclusões Regex e **Allowlists Inline (`pragma: allowlist secret`)**.
- [[detectsecrets-modo-slim-resolucao-conflitos-merge-monorepos-escala]] — Veja também: Operando `detect-secrets` em **Monorepos de Grande Escala**: Modo **`--slim`**, Execução Paralela Multi-Core e Varredura de Arquivos Não-Rastreados (`--all-files`).
- [[detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp]] — Referência cruzada direta com detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp.
- [[pacu-auditoria-lambda-env-vars-codigo-backdoor-api-gateway]] — Referência cruzada direta com pacu-auditoria-lambda-env-vars-codigo-backdoor-api-gateway.

## Fontes
- [Yelp `detect-secrets` Official GitHub — Enterprise Secret Detection, `.secrets.baseline`, Plugins & Filters](https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md) — documentação oficial do `detect-secrets` cobrindo `scan`, `audit`, `detect-secrets-hook`, os 27+ plugins detectores, filtros heurísticos e API Python `SecretsCollection`; consultado em 2026-10-03.
- [Yelp `detect-secrets` Official Pre-Commit Hook Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml) — especificação oficial do hook `detect-secrets-hook` para integração em pipelines e estações de desenvolvimento; consultado em 2026-10-03.
