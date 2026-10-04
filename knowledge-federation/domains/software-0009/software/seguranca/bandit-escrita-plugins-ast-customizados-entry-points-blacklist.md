---
id: software.seguranca.tranche03.000270
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst", "https://bandit.readthedocs.io/en/latest/config.html", "https://github.com/PyCQA/bandit"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Bandit Extensibilidade: criação de Plugins AST Customizados (`@test.checks('Call')`) para regras internas de segurança

## Em uma frase
A arquitetura do Bandit é 100% baseada em plugins registrados via `entry_points` (`bandit.plugins`) do Python: cada regra `Bxxx` é uma simples função Python decorada com **`@test.checks('Call')`** (ou `'Import'`, `'Str'`, `'Assign'`) e **`@test.test_id('B9xx')`** que recebe um objeto **`context`** e retorna um **`bandit.Issue(...)`** se detectar um padrão inseguro!

## Por que importa
Toda engenharia que mantém um framework Python interno possui convenções de segurança próprias (por exemplo: proibir chamadas diretas a `raw_sql_execute()` ou exigir que todo endpoint interno chame `@require_tenant_isolation`).

## Como funciona
No objeto `context` passado para o seu plugin pelo Bandit, métodos prontos como `context.call_function_name_qual` (nome totalmente qualificado da função chamada, já resolvendo imports!), `context.call_args`, `context.call_keywords` e `context.is_module_imported_like(...)` tornam a escrita de uma regra AST customizada uma tarefa de 15 linhas de Python!

## Exemplo
```python
import bandit
from bandit.core import issue
from bandit.core import test_properties as test

@test.checks("Call")
@test.test_id("B901")
def forbid_legacy_internal_crypto(context):
    if context.call_function_name_qual == "corp_legacy.crypto.encrypt_ecb":
        return bandit.Issue(
            severity=bandit.HIGH,
            confidence=bandit.HIGH,
            cwe=issue.Cwe.BROKEN_CRYPTO,
            text="O uso de corp_legacy.crypto.encrypt_ecb é proibido; utilize corp_security.aead.",
        )
```

## Limites e trade-offs
Registre seus plugins internos na faixa `B9xx` dentro de um pacote Python interno com o entry point `bandit.plugins` para que o binário `bandit` os descubra e execute automaticamente junto com as regras nativas.

## Como verificar
Execute `bandit --help` para verificar na lista final de plugins (`optional_plugins`) que seu teste `B901` foi carregado.

## Conexões
- [[bandit-formatos-relatorio-sarif-json-custom-pre-commit-ci]] — Veja também: Bandit Formatos de Saída (`json`, `sarif`, `xml`, `html`, `custom`) e Integração com `pre-commit` e GitHub Code Scanning.

## Fontes
- [PyCQA Bandit Official Documentation — Configuration (pyproject.toml, bandit.yaml, .bandit INI, Granular # nosec Exclusions & pre-commit Integration)](https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst) — Documentação oficial de configuração do Bandit detalhando arquivos INI/YAML/TOML, exclusões por ID no comentário # nosec e customização de plugins; consultado em 2026-10-03.
- [PyCQA Bandit GitHub — README.rst (Python AST Security Linter Architecture, Sigstore Cosign Container Verification & References)](https://bandit.readthedocs.io/en/latest/config.html) — README oficial do PyCQA/bandit apresentando a arquitetura de análise de nós AST em Python e verificação de imagens com Cosign; consultado em 2026-10-03.
- [PyCQA Bandit — Official GitHub Repository](https://github.com/PyCQA/bandit) — Repositório oficial Apache-2.0 do PyCQA Bandit; consultado em 2026-10-03.
