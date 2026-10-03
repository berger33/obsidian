---
id: software.devops.tranche17.001632
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://kubeedge.io/docs/architecture/cloud/cloudhub/", "https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md", "https://github.com/kubeedge/kubeedge"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# KubeEdge: comunicação bidirecional resiliente entre `CloudHub` e `EdgeHub` via WebSocket e QUIC

## Em uma frase
O `CloudHub` (módulo do `CloudCore` na nuvem) e o `EdgeHub` (módulo do `EdgeCore` no nó de borda) formam o barramento de comunicação multiplexado entre nuvem e borda, suportando conexões simultâneas sobre **HTTP/WebSocket** e protocolo **QUIC**.

## Por que importa
Nós de borda frequentemente operam atrás de NAT celular (4G/5G) ou redes satelitais com quedas frequentes de pacotes e troca de IP; conexões HTTP/2 padrão sofrem bloqueio head-of-line e não permitem que o plano de controle inicie conexões de entrada até o nó.

## Como funciona
O `EdgeHub` inicia a conexão de saída com TLS mútuo até o `CloudHub` (escolhendo WebSocket ou QUIC). No lado da nuvem, o `CloudHub` mantém uma fila de canais (`channelQ`) indexada por `nodeID`, converte mensagens JSON da borda em objetos de evento internos para o `EdgeController` e `DeviceController`, monitora *keepalive intervals* e publica eventos de falha caso o nó desconecte.

## Exemplo
```yaml
# Trecho de cloudcore.yaml
modules:
  cloudHub:
    advertiseAddress:
      - 203.0.113.10
    nodeLimit: 1000
    tlsCAFile: /etc/kubeedge/ca/rootCA.crt
    tlsCertFile: /etc/kubeedge/certs/server.crt
    tlsPrivateKeyFile: /etc/kubeedge/certs/server.key
    websocket:
      enable: true
      port: 10000
    quic:
      enable: true
      port: 10001
```

## Limites e trade-offs
O `CloudHub` pode ser configurado para rodar apenas o servidor WebSocket (porta padrão `10000`), apenas o servidor QUIC (porta padrão `10001`) ou ambos simultaneamente, devendo o endereço público da nuvem constar em `advertiseAddress`.

## Como verificar
Verifique nos logs do `cloudcore` (`kubectl logs -n kubeedge deploy/cloudcore`) o estabelecimento da sessão TLS/WebSocket ou QUIC para o `nodeID` do nó de borda.

## Conexões
- [[kubeedge-arquitetura-cloudcore-edgecore-cncf-graduated]] — Veja também: KubeEdge: arquitetura CNCF Graduated de computação de borda (`CloudCore` na nuvem e `EdgeCore` na borda).
- [[kubeedge-metamanager-sqlite-autonomia-offline-edged-recuperacao]] — Veja também: KubeEdge: autonomia de borda offline e recuperação pós-reboot via `MetaManager`, SQLite e `Edged`.

## Fontes
- [KubeEdge GitHub — README.md (CNCF Graduated Kubernetes Native Edge Computing Framework, CloudCore, EdgeCore, Mappers & EdgeMesh)](https://kubeedge.io/docs/architecture/cloud/cloudhub/) — README oficial do kubeedge/kubeedge (CNCF Graduated) descrevendo os módulos de nuvem (CloudHub, EdgeController, DeviceController) e de borda (Edged, MetaManager, DeviceTwin); consultado em 2026-10-03.
- [KubeEdge Official Documentation — Cloud Architecture: CloudHub (WebSocket & QUIC Servers, Keepalive & Dispatcher to EdgeHub)](https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md) — Documentação oficial de arquitetura do CloudHub no KubeEdge detalhando conexões WebSocket e QUIC, controle de sessão e multiplexação entre CloudCore e EdgeCore; consultado em 2026-10-03.
- [KubeEdge — Official GitHub Repository](https://github.com/kubeedge/kubeedge) — Repositório oficial Apache-2.0 do KubeEdge na CNCF; consultado em 2026-10-03.
