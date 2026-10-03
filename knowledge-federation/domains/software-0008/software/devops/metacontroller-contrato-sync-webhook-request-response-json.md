---
id: software.devops.tranche18.001774
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
fontes: ["https://metacontroller.github.io/metacontroller/concepts.html", "https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md", "https://github.com/metacontroller/metacontroller"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Metacontroller: contrato JSON de entrada e saída do webhook `sync` para reconciliação declarativa

## Em uma frase
O hook `sync` do Metacontroller opera como uma função pura de estado: ele recebe uma requisição HTTP `POST` contendo o estado observado (`parent` / `object` e `children` / `attachments` indexados por GVK e nome) e retorna uma resposta JSON declarando o `status` calculado e a lista completa de filhos desejados.

## Por que importa
Em controladores imperativos, o desenvolvedor precisa escrever chamadas separadas de `CREATE` se o filho não existir, `PATCH` se já existir e `DELETE` para os filhos que sobraram; no Metacontroller, basta retornar a lista de filhos desejados naquele instante.

## Como funciona
Ao receber a resposta `{ "status": {...}, "children": [...] }` do webhook, o próprio Metacontroller compara os objetos retornados com o cache local: cria os filhos que ainda não existem (injetando `ownerReferences` automaticamente), atualiza os filhos que mudaram (segundo a `updateStrategy` configurada) e deleta os filhos antigos que deixaram de figurar na lista retornada.

## Exemplo
```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SyncHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        observed = json.loads(self.rfile.read(int(self.headers.get('content-length'))))
        parent = observed['parent']
        desired_svc = {
            'apiVersion': 'v1',
            'kind': 'Service',
            'metadata': {'name': parent['metadata']['name']},
            'spec': {'ports': [{'port': 80}], 'selector': {'app': parent['metadata']['name']}},
        }
        body = json.dumps({'status': {'ready': True}, 'children': [desired_svc]}).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(body)
```

## Limites e trade-offs
Cuidado: se o seu webhook `sync` retornar `"children": []` (lista vazia) por engano, o Metacontroller interpretará que você deseja zero recursos filhos e deletará todos os filhos existentes daquele pai.

## Como verificar
Teste o endpoint Python do seu webhook localmente enviando um payload JSON de exemplo com `curl -X POST -d @sample-request.json` antes de conectá-lo ao Metacontroller.

## Conexões
- [[metacontroller-decoratorcontroller-attachments-labels-annotations]] — Veja também: Metacontroller `DecoratorController`: anexação de comportamentos e recursos secundários a objetos existentes.
- [[metacontroller-finalize-hook-limpeza-ordenada-finalizers]] — Veja também: Metacontroller `finalize` hook: gerenciamento declarativo de Finalizers e limpeza antes da exclusão.

## Fontes
- [Metacontroller GitHub — README.md (Lightweight Custom Controllers via JSON Webhooks in Any Language)](https://metacontroller.github.io/metacontroller/concepts.html) — README oficial do metacontroller/metacontroller apresentando escrita de controladores sem boilerplate em qualquer linguagem e instalação via Kustomize/Helm; consultado em 2026-10-03.
- [Metacontroller Official Documentation — Concepts (Canonical Plural Resources, API Groups/Versions/Kinds, Lambda Controllers & Hooks)](https://raw.githubusercontent.com/metacontroller/metacontroller/master/README.md) — Documentação oficial de conceitos do Metacontroller explicando recursos plurais canônicos, CompositeController, DecoratorController e hooks sync/finalize/customize; consultado em 2026-10-03.
- [Metacontroller — Official GitHub Repository](https://github.com/metacontroller/metacontroller) — Repositório oficial Apache-2.0 do Metacontroller; consultado em 2026-10-03.
