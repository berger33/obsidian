---
id: software.devops.tranche09.000886
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md", "https://telepresence.io/docs/concepts/architecture", "https://github.com/telepresenceio/telepresence"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Telepresence: dispositivo de rede virtual (VIF) no Root-Daemon, resolução DNS do cluster e roteamento direto de IPs

## Em uma frase
Ao executar `telepresence connect`, o `Root-Daemon` configura uma Virtual Network Interface (`VIF` / dispositivo `tun`) na estação de trabalho que roteia os CIDRs de Services e Pods do Kubernetes e resolve nomes DNS internos do cluster sem necessidade de `kubectl port-forward`.

## Por que importa
Usar `kubectl port-forward` para acessar 5 microsserviços e 2 bancos de dados diferentes no cluster exige abrir 7 terminais paralelos mapeando portas arbitrárias (`localhost:15432`, `localhost:18081`), quebrando a descoberta de serviços por DNS (`postgres.db.svc.cluster.local:5432`) e os certificados TLS que validam o hostname real do Service. O README oficial (`Cluster access`) e a página `Architecture` explicam como a VIF resolve isso.

## Como funciona
Quando `telepresence connect` é executado, o `User-Daemon` conecta-se ao `Traffic Manager` no cluster para descobrir as sub-redes (CIDRs) de `Services` e `Pods` e o servidor DNS interno (`CoreDNS`). Em seguida, o **`Root-Daemon`** cria uma interface de rede virtual (**`VIF`**) no sistema operacional da estação de trabalho, adiciona rotas de tabela de rede direcionando os CIDRs do cluster para a VIF e integra um resolvedor DNS local. Assim, qualquer aplicação na estação de trabalho (navegador, `curl`, `psql`, cliente gRPC ou código na IDE) pode conectar-se diretamente a `http://orders.prod.svc.cluster.local` (ou apenas `http://orders` se conectado com `--namespace prod`) nas portas originais.

## Exemplo
```bash
# Conectar ao cluster fixando o namespace padrão de resolução DNS e verificar as sub-redes roteadas pela VIF
telepresence connect --namespace staging
telepresence status
```

## Limites e trade-offs
Se a sub-rede CIDR de Pods ou Services do cluster Kubernetes remoto (por exemplo, `10.0.0.0/8` ou `172.16.0.0/12`) colidir com a faixa de IPs da rede Wi-Fi local ou da VPN corporativa da estação de trabalho do desenvolvedor, rotear o CIDR inteiro pela VIF pode causar conflito de rotas; nesses casos, o Telepresence permite configurar `alsoProxy` / `neverProxy` no Helm chart do `Traffic Manager` ou usar `telepresence connect --docker` para isolar a rede virtual dentro de um container Docker local.

## Como verificar
Execute `telepresence status` e confirme na seção `Root Daemon` as faixas de sub-redes (`Subnets`) mapeadas na interface virtual e o funcionamento de `nslookup kubernetes.default.svc.cluster.local`.

## Conexões
- [[telepresence-ambiente-remoto-variaveis-montagem-volumes-locais]] — Veja também: Telepresence: importação de variáveis de ambiente (--env-file) e montagem de volumes remotos (--mount) no processo local.
- [[telepresence-execucao-containers-docker-run-docker-build]] — Veja também: Telepresence: execução de interceptações em containers Docker locais (--docker-run, --docker-build e telepresence connect --docker).
- [[telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura]] — Referência cruzada direta com telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura.
- [[minikube-exposicao-servicos-service-nodeport-tunnel-loadbalancer]] — Referência cruzada direta com minikube-exposicao-servicos-service-nodeport-tunnel-loadbalancer.

## Fontes
- [Telepresence GitHub — README.md (CNCF Local-to-Cluster Development, 4 Attachment Modes & Traffic Filtering)](https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md) — README oficial do Telepresence (v2) detalhando eliminação do ciclo build/push/deploy, modos replace/intercept/wiretap/ingest, filtragem HTTP para equipes e importação de ambiente/volumes; consultado em 2026-10-03.
- [Telepresence Official Documentation — Architecture (User-Daemon, Root-Daemon VIF, Traffic Manager & Sidecar vs Node-Agent)](https://telepresence.io/docs/concepts/architecture) — Documentação oficial de arquitetura do Telepresence v2.32 explicando User-Daemon, Root-Daemon (Virtual Network Device VIF), Traffic Manager (telepresence helm install) e Traffic Agent como sidecar ou node-agent sem restart; consultado em 2026-10-03.
- [Telepresence — Official GitHub Repository](https://github.com/telepresenceio/telepresence) — Repositório oficial Apache-2.0 do Telepresence na CNCF; consultado em 2026-10-03.
