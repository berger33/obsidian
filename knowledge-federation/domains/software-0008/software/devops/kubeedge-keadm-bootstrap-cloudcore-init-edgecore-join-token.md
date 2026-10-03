---
id: software.devops.tranche17.001639
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

# KubeEdge: provisionamento de plano de controle e nós de borda com o instalador `keadm`

## Em uma frase
O `keadm` é a ferramenta oficial de linha de comando do KubeEdge para instalar o `CloudCore` em um cluster Kubernetes existente (`keadm init`) e ingressar nós de borda (`keadm join`) usando tokens de bootstrap autenticados.

## Por que importa
Configurar manualmente os CRDs `devices`/`rules`/`reliablesyncs`, gerar certificados TLS para `CloudHub`/`CloudStream` e instalar os binários e serviços systemd do `EdgeCore` em centenas de gateways ARM/x86 é complexo e sujeito a erros.

## Como funciona
No lado da nuvem, `keadm init --advertise-address=<IP-Publico>` aplica os CRDs e implanta o `CloudCore`; em seguida, `keadm gettoken` extrai o token criptográfico de registro. No gateway de borda (com `containerd` instalado), basta executar `keadm join --cloudcore-ipport=<IP>:10000 --token=<token>` para baixar a versão compatível do `EdgeCore`, gerar `edgecore.yaml` e iniciar o serviço systemd.

## Exemplo
```bash
# Na nuvem:
keadm init --advertise-address="203.0.113.10" --kubeedge-version=v1.20.0
TOKEN=$(keadm gettoken)

# No nó de borda:
keadm join --cloudcore-ipport="203.0.113.10:10000" --token="$TOKEN" --kubeedge-version=v1.20.0
```

## Limites e trade-offs
Sempre consulte a tabela de compatibilidade de versões do KubeEdge contra a versão do Kubernetes antes do `keadm init` (por exemplo, KubeEdge `1.20` é exatamente compatível com Kubernetes `1.28`–`1.30`, enquanto KubeEdge `1.23` cobre `1.30`–`1.32`).

## Como verificar
Execute `keadm gettoken` na nuvem e, após rodar `keadm join` no host de borda, verifique `systemctl is-active edgecore` e `kubectl get nodes`.

## Conexões
- [[kubeedge-edgemesh-comunicacao-pod-a-pod-cross-subnet-logs-exec]] — Veja também: KubeEdge: `EdgeMesh` e `CloudStream`/`EdgeStream` para rede Pod-a-Pod entre bordas e `kubectl logs`/`exec`.
- [[kubeedge-reliablesyncs-objectsync-garantia-entrega-sem-perda]] — Veja também: KubeEdge: entrega confiável de mensagens sem perda sobre redes instáveis via `ObjectSync` (`reliablesyncs`).

## Fontes
- [KubeEdge GitHub — README.md (CNCF Graduated Kubernetes Native Edge Computing Framework, CloudCore, EdgeCore, Mappers & EdgeMesh)](https://raw.githubusercontent.com/kubeedge/kubeedge/master/README.md) — README oficial do kubeedge/kubeedge (CNCF Graduated) descrevendo os módulos de nuvem (CloudHub, EdgeController, DeviceController) e de borda (Edged, MetaManager, DeviceTwin); consultado em 2026-10-03.
- [KubeEdge Official Documentation — Cloud Architecture: CloudHub (WebSocket & QUIC Servers, Keepalive & Dispatcher to EdgeHub)](https://kubeedge.io/docs/architecture/cloud/cloudhub/) — Documentação oficial de arquitetura do CloudHub no KubeEdge detalhando conexões WebSocket e QUIC, controle de sessão e multiplexação entre CloudCore e EdgeCore; consultado em 2026-10-03.
- [KubeEdge — Official GitHub Repository](https://github.com/kubeedge/kubeedge) — Repositório oficial Apache-2.0 do KubeEdge na CNCF; consultado em 2026-10-03.
