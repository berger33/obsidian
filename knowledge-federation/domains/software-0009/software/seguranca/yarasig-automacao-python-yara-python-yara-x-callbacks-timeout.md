---
id: software.seguranca.tranche03.000289
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
fontes: ["https://raw.githubusercontent.com/VirusTotal/yara/master/README.md", "https://yara.readthedocs.io/en/stable/writingrules.html", "https://github.com/VirusTotal/yara"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# YARA Automação em Python (`yara-python` e `yara_x`): compilação em memória, callbacks de `matches` e proteção por `timeout`

## Em uma frase
Conforme destacado no README oficial (*"can be used through its command-line interface or from your own Python scripts with the yara-python extension"*), os bindings oficiais **`yara-python`** (e **`yara-x`** para Python) permitem embutir o motor YARA diretamente em pipelines de triagem de uploads web, sandboxes de malware, workers Celery e lambdas serverless.

## Por que importa
Invocar um subprocesso `os.system("yara ...")` para cada arquivo enviado por usuários em uma API de upload tem alto custo de criação de processo; com `yara.compile(...)` em memória na inicialização do worker Python, cada `rules.match(data=buffer, timeout=10)` executa em microssegundos direto sobre o buffer em RAM sem gravar o arquivo suspeito no disco!

## Como funciona
Sempre passe o parâmetro **`timeout=`** (em segundos, ex.: `timeout=15`) na chamada `rules.match(...)` ao escanear arquivos enviados por usuários externos para garantir que um arquivo construído maliciosamente nunca prenda o worker por tempo excessivo.

## Exemplo
```python
import yara

# Compilando regras uma única vez na inicialização do worker e escaneando buffers em memória com timeout:
RULES = yara.compile(source="""
rule Detect_WebShell_Upload {
    strings:
        $php = "<?php" ascii nocase
        $eval = "eval(base64_decode(" ascii nocase
        $sys = "shell_exec(" ascii nocase
    condition:
        $php and ($eval or $sys)
}
""")

def scan_uploaded_bytes(payload: bytes) -> list[str]:
    matches = RULES.match(data=payload, timeout=10)
    return [m.rule for m in matches]
```

## Limites e trade-offs
Quando usar `fast=True` em `rules.match(data=payload, fast=True)` (equivalente à flag `-f` da CLI), o YARA para de buscar novas ocorrências da mesma string assim que encontra a primeira (útil quando suas regras não usam o operador de contagem `#a`).

## Como verificar
Execute um teste unitário em Python validando `scan_uploaded_bytes(b"<?php eval(base64_decode('...'));")`.

## Conexões
- [[yarasig-otimizacao-performance-atoms-aho-corasick-regex-bounded-profiling]] — Veja também: YARA Engenharia de Performance: escolha de *Atoms* para o motor Aho-Corasick, perigos de Regex abertas (`.*`) e `short-circuit`.
- [[yarasig-ecossistema-yarahq-yara-forge-yargen-yara-ci-integracoes]] — Veja também: YARA no Ecossistema DFIR/SOC: integração com `Velociraptor`, `osquery`, `ClamAV`, `LimaCharlie` e curadoria com `YARA-CI` / `YARA Forge`.

## Fontes
- [YARA Official Documentation — Writing YARA Rules (Rule Anatomy, Hexadecimal Wildcards/Not/Jumps/Alternatives, Text Modifiers, Conditions & Modules)](https://raw.githubusercontent.com/VirusTotal/yara/master/README.md) — Guia oficial completo de escrita de regras YARA cobrindo palavras-chave reservadas, strings hexadecimais e textuais, condições, offsets e modularização; consultado em 2026-10-03.
- [VirusTotal YARA GitHub — README.md (Pattern Matching Engine Overview, Rule Syntax, YARA-X Transition, yara-python & Ecosystem)](https://yara.readthedocs.io/en/stable/writingrules.html) — README oficial do VirusTotal/yara apresentando o projeto, integração com yara-python, YARA-CI e transição para o YARA-X em Rust; consultado em 2026-10-03.
- [VirusTotal YARA — Official GitHub Repository](https://github.com/VirusTotal/yara) — Repositório oficial BSD-3-Clause do VirusTotal YARA; consultado em 2026-10-03.
