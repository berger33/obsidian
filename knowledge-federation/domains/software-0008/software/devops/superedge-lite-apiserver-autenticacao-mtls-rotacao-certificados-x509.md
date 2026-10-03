---
id: software.devops.tranche17.001658
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

# SuperEdge `lite-apiserver`: autenticação multi-cliente (X.509 mTLS, Bearer Token) e suporte a rotação de certificados

## Em uma frase
O `lite-apiserver` autentica e isola o cache de múltiplos clientes locais no mesmo nó de borda — tanto componentes de host que usam certificados de cliente X.509 (`kubelet`, `kube-proxy`) quanto Pods em execução que usam Bearer Tokens de `ServiceAccount` — suportando rotação automática de certificados do `kubelet`.

## Por que importa
Se um proxy local de borda compartilhasse uma única conexão ou retornasse objetos cacheados sem distinguir a identidade de quem está pedindo, um Pod sem privilégios poderia ler dados que o `kubelet` baixou ou a rotação periódica do certificado `/var/lib/kubelet/pki/kubelet-client-current.pem` quebraria o proxy.

## Como funciona
O `lite-apiserver` extrai o `Common Name` do certificado TLS apresentado na conexão (ou o hash do Bearer Token para requisições sem certificado mTLS) para selecionar o `ReverseProxy` e a partição de cache apropriados, além de recarregar dinamicamente os certificados rotacionados pelo `kubelet`.

## Exemplo
```bash
# Verificando os certificados usados pelo kubelet junto ao lite-apiserver no nó de borda:
ls -l /var/lib/kubelet/pki/kubelet-client-current.pem
```

## Limites e trade-offs
Para que os Pods da aplicação (como operadores ou agentes rodando na borda) também se beneficiem do cache offline do `lite-apiserver`, o endereço da variável de ambiente `KUBERNETES_SERVICE_HOST`/`PORT` injetada nos Pods na borda é direcionado para o `lite-apiserver` local.

## Como verificar
Inspecione as variáveis `KUBERNETES_SERVICE_HOST` e `KUBERNETES_SERVICE_PORT` dentro de um Pod rodando em um nó de borda do SuperEdge.

## Conexões
- [[superedge-site-manager-nodeunit-nodegroup-modelagem-topologica]] — Veja também: SuperEdge `site-manager`: modelagem topológica de sites com `NodeUnit` e `NodeGroup`.
- [[superedge-edgeadm-instalacao-offline-conversao-cluster-nativo]] — Veja também: SuperEdge `edgeadm`: instalação one-click offline de clusters de borda e conversão de clusters Kubernetes nativos.

## Fontes
- [SuperEdge GitHub — README.md (Kubernetes-Native Edge Container Management System, Kins L4/L5 Autonomy, ServiceGroup & Edge-Health)](https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md) — README oficial do superedge/superedge detalhando componentes de nuvem e borda, níveis de autonomia L3/L4/L5 (Kins), DeploymentGrid/ServiceGrid, tunnel e edgeadm; consultado em 2026-10-03.
- [SuperEdge Official Documentation — Components: lite-apiserver (TLS CN Reverse Proxy, Bolt/Badger/File Cache & Certificate Rotation)](https://raw.githubusercontent.com/superedge/superedge/main/README.md) — Documentação técnica oficial do componente lite-apiserver no SuperEdge cobrindo proxy por Common Name X.509, motores de cache local e autonomia L3; consultado em 2026-10-03.
- [SuperEdge — Official GitHub Repository](https://github.com/superedge/superedge) — Repositório oficial Apache-2.0 do SuperEdge; consultado em 2026-10-03.
