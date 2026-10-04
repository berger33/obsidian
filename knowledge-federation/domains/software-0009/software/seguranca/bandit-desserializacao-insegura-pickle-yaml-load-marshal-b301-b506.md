---
id: software.seguranca.tranche03.000265
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

# Bandit Desserialização Insegura e XML (`B301` `pickle`, `B506` `yaml.load`, `B314`–`B320` XXE `defusedxml`)

## Em uma frase
Os plugins **`B301` (`pickle`)**, **`B302` (`marshal`)**, **`B403` (`import_pickle`)**, **`B506` (`yaml_load`)** e **`B314`–`B320` / `B405`–`B411` (`xml_*`)** do Bandit detectam o uso de desserializadores e parsers XML vulneráveis a Execução Remota de Código (RCE) e *XML External Entity (XXE)* em aplicações Python.

## Por que importa
Em Python, chamar `pickle.loads(data)` sobre bytes não confiáveis permite execução imediata de código arbitrário via método mágico `__reduce__`; da mesma forma, chamar `yaml.load(stream, Loader=yaml.Loader)` (ou sem `SafeLoader`) permite instanciar objetos Python arbitrários (`!!python/object/apply:os.system`), e os parsers XML padrão (`xml.etree.ElementTree`, `xml.dom.minidom`) são vulneráveis a bombas de entidades (*Billion Laughs*) ou XXE.

## Como funciona
O Bandit exige o uso de **`yaml.safe_load()`** (ou `Loader=yaml.SafeLoader`), formatos seguros de dados (`json`, `msgpack`, `protobuf`) em vez de `pickle` para dados externos, e o pacote **`defusedxml`** para qualquer parsing de XML não confiável!

## Exemplo
```python
import yaml
import defusedxml.ElementTree as ET

def parse_configs_safely(yaml_str: str, xml_str: str):
    # SEGURO (aprovado pelo B506 e B314): usa yaml.safe_load e defusedxml
    cfg = yaml.safe_load(yaml_str)
    root = ET.fromstring(xml_str)
    return cfg, root
```

## Limites e trade-offs
Em pipelines de Machine Learning / IA que carregam pesos de modelos PyTorch/ NumPy da internet, evite formatos baseados em `pickle` puro: prefira **`safetensors`** ou passe `weights_only=True` no `torch.load`.

## Como verificar
Execute `bandit -t B301,B506 -r .` para auditar chamadas de desserialização em todo o repositório.

## Conexões
- [[bandit-injecao-comandos-subprocess-shell-true-b602-b605-os-system]] — Veja também: Bandit Prevenção de Command Injection (`B602`–`B607`): `subprocess` com `shell=True`, `os.system` e customização do plugin.
- [[bandit-criptografia-fraca-random-hashes-md5-sha1-tls-b303-b311-b501]] — Veja também: Bandit Criptografia, PRNG e TLS (`B303`/`B324` MD5/SHA1, `B311` `random` vs `secrets`, `B501` `verify=False` e `B502` SSL/TLS).

## Fontes
- [PyCQA Bandit Official Documentation — Configuration (pyproject.toml, bandit.yaml, .bandit INI, Granular # nosec Exclusions & pre-commit Integration)](https://raw.githubusercontent.com/PyCQA/bandit/main/README.rst) — Documentação oficial de configuração do Bandit detalhando arquivos INI/YAML/TOML, exclusões por ID no comentário # nosec e customização de plugins; consultado em 2026-10-03.
- [PyCQA Bandit GitHub — README.rst (Python AST Security Linter Architecture, Sigstore Cosign Container Verification & References)](https://bandit.readthedocs.io/en/latest/config.html) — README oficial do PyCQA/bandit apresentando a arquitetura de análise de nós AST em Python e verificação de imagens com Cosign; consultado em 2026-10-03.
- [PyCQA Bandit — Official GitHub Repository](https://github.com/PyCQA/bandit) — Repositório oficial Apache-2.0 do PyCQA Bandit; consultado em 2026-10-03.
