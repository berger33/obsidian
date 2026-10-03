---
id: software.devops.tranche16.001507
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://carvel.dev/ytt/docs/v0.52.x/", "https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md", "https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel ytt: módulos Starlark embutidos (`@ytt:json`, `@ytt:yaml`, `@ytt:base64`, `@ytt:sha256`, `@ytt:regexp`)

## Em uma frase
O `ytt` disponibiliza uma biblioteca padrão de módulos determinísticos (`@ytt:json`, `@ytt:yaml`, `@ytt:base64`, `@ytt:sha256`, `@ytt:md5`, `@ytt:regexp`, `@ytt:url`, `@ytt:version`) para serializar configurações embutidas em `ConfigMap`/`Secret` e calcular hashes de rollout.

## Por que importa
Muitas aplicações leem arquivos `config.json` ou `app.yaml` montados a partir de um `ConfigMap`, além de exigirem uma anotação de checksum SHA-256 no template do Pod para acionar rollouts automáticos quando o conteúdo da configuração muda.

## Como funciona
Em vez de manter strings JSON ou YAML escapadas manualmente dentro de um `ConfigMap`, o autor define a estrutura como um dicionário nativo no `ytt`, usa `yaml.encode(...)` ou `json.encode(...)` para preencher a chave do `ConfigMap` e calcula `sha256.sum(...)` sobre o mesmo conteúdo para injetar na anotação `checksum/config` do `Deployment`.

## Exemplo
```yaml
#@ load("@ytt:yaml", "yaml")
#@ load("@ytt:sha256", "sha256")

#@ app_cfg = {"server": {"port": 8080, "tls": True}, "log_level": "info"}
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  config.yaml: #@ yaml.encode(app_cfg)
  config.sha256: #@ sha256.sum(yaml.encode(app_cfg))
```

## Limites e trade-offs
Por garantia de determinismo e segurança de sandbox, o `ytt` não inclui funções para gerar UUIDs aleatórios, ler variáveis de ambiente do host sem flags explícitas ou consultar timestamps do relógio do sistema.

## Como verificar
Execute `ytt -f configmap-hash.yml` duas vezes consecutivas e confirme que o `config.sha256` gerado é idêntico bit a bit em ambas as execuções.

## Conexões
- [[carvel-ytt-bibliotecas-privadas-ytt-lib-module-instanciacao]] — Veja também: Carvel ytt: bibliotecas privadas (`_ytt_lib`) e instanciação programática via `@ytt:library`.
- [[carvel-ytt-precedencia-valores-data-values-file-env-flags]] — Veja também: Carvel ytt: ordem de precedência e injeção de Data Values via arquivos, variáveis de ambiente e flags CLI.

## Fontes
- [Carvel ytt GitHub — README.md (Structural YAML Templating, Starlark, Custom Validations, Overlays & Sandboxing)](https://carvel.dev/ytt/docs/v0.52.x/) — README oficial do carvel-dev/ytt detalhando templating estrutural ciente de YAML, linguagem Starlark determinística, overlays e validações; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — About ytt v0.52.x (Templating, Data Values, Patching/Overlaying & Modularizing)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md) — Documentação oficial do Carvel ytt explicando anotações #@, Data Values, módulo @ytt:overlay, fragmentos YAML e bibliotecas _ytt_lib; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — Application Programming Interfaces of ytt (Executable vs Go Module Integration)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md) — Guia oficial de integração do Carvel ytt comparando invocação como executável externo versus módulo Go in-process; consultado em 2026-10-03.
