---
id: software.devops.tranche16.001506
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

# Carvel ytt: bibliotecas privadas (`_ytt_lib`) e instanciação programática via `@ytt:library`

## Em uma frase
O mecanismo de bibliotecas do `ytt` (`_ytt_lib` e `@ytt:library`) permite empacotar conjuntos completos de templates, esquemas e overlays em unidades isoladas que podem ser instanciadas múltiplas vezes com diferentes valores dentro de uma mesma execução.

## Por que importa
Quando uma aplicação composta precisa instanciar três bancos de dados ou múltiplos subcomponentes baseados no mesmo pacote de templates, variáveis globais compartilhadas colidiriam se todos os arquivos fossem avaliados em um único escopo plano.

## Como funciona
Todo diretório colocado dentro de `_ytt_lib/<nome-da-lib>/` permanece inativo na avaliação principal até ser carregado explicitamente com `library.get("<nome-da-lib>")`. O template consumidor pode então aplicar valores customizados (`lib.with_data_values(...)`) e overlays específicos (`lib.with_ague(...)`) e chamar `.eval()` para emitir os documentos YAML daquela instância isolada.

## Exemplo
```yaml
#@ load("@ytt:library", "library")
#@ load("@ytt:template", "template")

#@ redis_cache = library.get("redis").with_data_values({"name": "redis-cache", "port": 6379})
#@ redis_queue = library.get("redis").with_data_values({"name": "redis-queue", "port": 6380})
--- #@ template.replace(redis_cache.eval())
--- #@ template.replace(redis_queue.eval())
```

## Limites e trade-offs
Arquivos localizados dentro de `_ytt_lib` não são renderizados automaticamente quando se passa o diretório raiz para `ytt -f .`; eles exigem invocação explícita via `@ytt:library` ou referência direta ao subdiretório.

## Como verificar
Crie uma estrutura com `_ytt_lib/redis/config.yml`, execute `ytt -f .` e verifique que duas instâncias independentes (`redis-cache` e `redis-queue`) são emitidas na saída.

## Conexões
- [[carvel-ytt-modularizacao-funcoes-fragmentos-yaml-load]] — Veja também: Carvel ytt: modularização com funções Starlark, fragmentos YAML e `load()`.
- [[carvel-ytt-bibliotecas-embutidas-json-yaml-base64-sha256-regexp]] — Veja também: Carvel ytt: módulos Starlark embutidos (`@ytt:json`, `@ytt:yaml`, `@ytt:base64`, `@ytt:sha256`, `@ytt:regexp`).

## Fontes
- [Carvel ytt GitHub — README.md (Structural YAML Templating, Starlark, Custom Validations, Overlays & Sandboxing)](https://carvel.dev/ytt/docs/v0.52.x/) — README oficial do carvel-dev/ytt detalhando templating estrutural ciente de YAML, linguagem Starlark determinística, overlays e validações; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — About ytt v0.52.x (Templating, Data Values, Patching/Overlaying & Modularizing)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md) — Documentação oficial do Carvel ytt explicando anotações #@, Data Values, módulo @ytt:overlay, fragmentos YAML e bibliotecas _ytt_lib; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — Application Programming Interfaces of ytt (Executable vs Go Module Integration)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md) — Guia oficial de integração do Carvel ytt comparando invocação como executável externo versus módulo Go in-process; consultado em 2026-10-03.
