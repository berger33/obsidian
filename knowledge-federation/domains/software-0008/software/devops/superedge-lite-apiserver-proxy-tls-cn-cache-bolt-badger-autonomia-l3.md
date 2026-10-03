---
id: software.devops.tranche17.001652
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
fontes: ["https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md", "https://raw.githubusercontent.com/superedge/superedge/main/README.md", "https://github.com/superedge/superedge"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SuperEdge `lite-apiserver`: proxy HTTPS por Common Name TLS e cache persistente (`file`, `bolt`, `badger`) para autonomia L3

## Em uma frase
O `lite-apiserver` é um servidor HTTPS leve que roda como Pod estático ou serviço systemd em cada nó de borda do SuperEdge, atuando como proxy reverso e cache persistente entre todos os componentes do nó (`kubelet`, `kube-proxy`, CNI, Pods) e o `kube-apiserver` da nuvem.

## Por que importa
Quando a conexão entre o nó de borda e a nuvem cai (e ainda mais se o servidor de borda reiniciar durante o apagão de rede), o `kubelet` e os Pods que dependem da API do Kubernetes falhariam por timeout se não houvesse um cache local capaz de autenticar e responder às requisições GET/LIST.

## Como funciona
O `lite-apiserver` inspeciona o `Common Name` (CN) do certificado X.509 mTLS de cada cliente local (ou Bearer Token, suportando rotação automática de certificados) e usa um `ReverseProxy` dedicado para encaminhar a chamada ao `kube-apiserver`. Quando a rede está normal, ele armazena assincronamente a resposta em disco (`file` ou bancos KV `bolt` / `badger`); quando a requisição à nuvem dá timeout, o `lite-apiserver` consulta e retorna os dados do cache local (autonomia nível L3), cobrindo recursos nativos e CRDs.

## Exemplo
```bash
# No nó de borda, testando a autonomia L3 durante desconexão:
systemctl status lite-apiserver
curl -k https://127.0.0.1:51003/healthz
```

## Limites e trade-offs
No nível de autonomia L3 provido pelo `lite-apiserver`, o nó de borda continua operando e sobrevive a reboots totalmente desconectado, mas não pode executar operações de escrita na API (`create`, `update`, `delete`) enquanto estiver offline da nuvem.

## Como verificar
Implante um Deployment `echoserver` no nó de borda, desconecte a rede até o `kube-apiserver`, reinicie o nó de borda e valide com `curl http://<pod-ip>:8080` que o Pod voltou a rodar autonomamente.

## Conexões
- [[superedge-arquitetura-edge-computing-cloud-edge-componentes]] — Veja também: SuperEdge: arquitetura de gerenciamento de containers em múltiplas regiões de borda.
- [[superedge-kins-k3s-in-superedge-autonomia-l4-l5-nodeunit-offline]] — Veja também: SuperEdge `Kins` (*K3s in SuperEdge*): autonomia de borda L4 e L5 com clusters K3s leves por `NodeUnit`.

## Fontes
- [SuperEdge GitHub — README.md (Kubernetes-Native Edge Container Management System, Kins L4/L5 Autonomy, ServiceGroup & Edge-Health)](https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md) — README oficial do superedge/superedge detalhando componentes de nuvem e borda, níveis de autonomia L3/L4/L5 (Kins), DeploymentGrid/ServiceGrid, tunnel e edgeadm; consultado em 2026-10-03.
- [SuperEdge Official Documentation — Components: lite-apiserver (TLS CN Reverse Proxy, Bolt/Badger/File Cache & Certificate Rotation)](https://raw.githubusercontent.com/superedge/superedge/main/README.md) — Documentação técnica oficial do componente lite-apiserver no SuperEdge cobrindo proxy por Common Name X.509, motores de cache local e autonomia L3; consultado em 2026-10-03.
- [SuperEdge — Official GitHub Repository](https://github.com/superedge/superedge) — Repositório oficial Apache-2.0 do SuperEdge; consultado em 2026-10-03.
