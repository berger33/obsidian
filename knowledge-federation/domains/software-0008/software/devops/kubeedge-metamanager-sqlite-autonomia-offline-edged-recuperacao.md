---
id: software.devops.tranche17.001633
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
fontes: ["https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md", "https://kubeedge.io/docs/architecture/cloud/cloudhub/", "https://github.com/kubeedge/kubeedge"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# KubeEdge: autonomia de borda offline e recuperação pós-reboot via `MetaManager`, SQLite e `Edged`

## Em uma frase
No nó de borda, o módulo `MetaManager` atua como processador de mensagens entre o `EdgeHub` e o `Edged`, persistindo todos os metadados de Pods, ConfigMaps, Secrets e dispositivos em um banco de dados leve **SQLite** local.

## Por que importa
Quando o link entre uma fábrica/filial e a nuvem cai, ou se o gateway de borda sofrer queda de energia e reiniciar enquanto a internet ainda estiver fora do ar, os containers locais precisam reiniciar imediatamente sem depender do `kube-apiserver` remoto.

## Como funciona
Toda atualização recebida da nuvem pelo `EdgeHub` é gravada no SQLite local pelo `MetaManager` antes de ser entregue ao `Edged`. Se o link nuvem-borda cair ou o nó de borda reiniciar offline, o `Edged` lê os manifestos e segredos diretamente do SQLite local via `MetaManager` e reconstrói todos os Pods autonomamente, além de evitar que o plano de controle evicte os Pods daquele nó durante a desconexão.

## Exemplo
```bash
systemctl status edgecore
ls -lh /var/lib/kubeedge/edgecore.db
sqlite3 /var/lib/kubeedge/edgecore.db "SELECT key FROM meta LIMIT 10;"
```

## Limites e trade-offs
Se um Pod agendado para um nó de borda referenciar uma imagem de container que ainda não está no cache local do `containerd` do nó e a internet cair antes do pull inicial, a autonomia do `MetaManager` terá o manifesto YAML no SQLite, mas o container ficará aguardando o retorno da rede para baixar os blobs.

## Como verificar
Inspecione a tabela `meta` em `/var/lib/kubeedge/edgecore.db` no nó de borda e teste reiniciar o serviço `edgecore` com a interface WAN desconectada para comprovar a manutenção dos Pods.

## Conexões
- [[kubeedge-cloudhub-edgehub-websocket-quic-channelq-mensageria]] — Veja também: KubeEdge: comunicação bidirecional resiliente entre `CloudHub` e `EdgeHub` via WebSocket e QUIC.
- [[kubeedge-edgecontroller-sincronizacao-pods-nodes-configmaps-secrets]] — Veja também: KubeEdge: sincronização bidirecional de metadados Kubernetes pelo `EdgeController`.

## Fontes
- [KubeEdge GitHub — README.md (CNCF Graduated Kubernetes Native Edge Computing Framework, CloudCore, EdgeCore, Mappers & EdgeMesh)](https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md) — README oficial do kubeedge/kubeedge (CNCF Graduated) descrevendo os módulos de nuvem (CloudHub, EdgeController, DeviceController) e de borda (Edged, MetaManager, DeviceTwin); consultado em 2026-10-03.
- [KubeEdge Official Documentation — Cloud Architecture: CloudHub (WebSocket & QUIC Servers, Keepalive & Dispatcher to EdgeHub)](https://kubeedge.io/docs/architecture/cloud/cloudhub/) — Documentação oficial de arquitetura do CloudHub no KubeEdge detalhando conexões WebSocket e QUIC, controle de sessão e multiplexação entre CloudCore e EdgeCore; consultado em 2026-10-03.
- [KubeEdge — Official GitHub Repository](https://github.com/kubeedge/kubeedge) — Repositório oficial Apache-2.0 do KubeEdge na CNCF; consultado em 2026-10-03.
