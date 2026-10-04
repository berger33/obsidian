---
id: software.devops.tranche17.001659
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
fontes: ["https://raw.githubusercontent.com/superedge/superedge/main/README.md", "https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md", "https://github.com/superedge/superedge"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SuperEdge `edgeadm`: instalação one-click offline de clusters de borda e conversão de clusters Kubernetes nativos

## Em uma frase
A ferramenta `edgeadm` do projeto SuperEdge permite tanto provisionar um cluster Kubernetes de borda completo do zero usando pacotes `.tar.gz` offline (`--install-pkg-path`) quanto converter um cluster Kubernetes padrão já existente em um cluster SuperEdge.

## Por que importa
Locais de borda industrial frequentemente possuem acesso restrito ou lento a repositórios públicos de pacotes Linux e registries internacionais no momento do bootstrap inicial dos servidores (`x86_64` ou `arm64`).

## Como funciona
O pacote `edgeadm-linux-<arch>-<version>` embute o binário `edgeadm` e os artefatos `kube-linux-*.tar.gz`. Com `./edgeadm init --install-pkg-path ./kube-linux-*.tar.gz --enable-edge=true`, o instalador configura o runtime, o control plane e todos os manifestos do SuperEdge; alternativamente, o comando `edgeadm addon` instala os componentes do SuperEdge sobre um cluster `kubeadm` existente.

## Exemplo
```bash
./edgeadm join 198.51.100.10:6443 \
  --token xxxx \
  --discovery-token-ca-cert-hash sha256:xxxxxxxxxx \
  --install-pkg-path ./kube-linux-amd64.tar.gz \
  --enable-edge=true
```

## Limites e trade-offs
Ao inicializar o master com `./edgeadm init`, lembre-se de informar tanto `--apiserver-advertise-address=<IP-Intranet>` quanto `--apiserver-cert-extra-sans=<IP-Publico-ou-Dominio>` para que os nós de borda remotos validem o certificado TLS do `kube-apiserver` pela internet.

## Como verificar
Verifique os SANs do certificado gerado em `/etc/kubernetes/pki/apiserver.crt` com `openssl x509 -in /etc/kubernetes/pki/apiserver.crt -noout -text | grep -A1 "Subject Alternative Name"`.

## Conexões
- [[superedge-lite-apiserver-autenticacao-mtls-rotacao-certificados-x509]] — Veja também: SuperEdge `lite-apiserver`: autenticação multi-cliente (X.509 mTLS, Bearer Token) e suporte a rotação de certificados.
- [[superedge-canary-upgrades-multi-regiao-statefulsetgrid-servicegrid]] — Veja também: SuperEdge: atualizações graduais por região com `StatefulSetGrid` e templates diferenciados por `NodeUnit`.

## Fontes
- [SuperEdge GitHub — README.md (Kubernetes-Native Edge Container Management System, Kins L4/L5 Autonomy, ServiceGroup & Edge-Health)](https://raw.githubusercontent.com/superedge/superedge/main/README.md) — README oficial do superedge/superedge detalhando componentes de nuvem e borda, níveis de autonomia L3/L4/L5 (Kins), DeploymentGrid/ServiceGrid, tunnel e edgeadm; consultado em 2026-10-03.
- [SuperEdge Official Documentation — Components: lite-apiserver (TLS CN Reverse Proxy, Bolt/Badger/File Cache & Certificate Rotation)](https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md) — Documentação técnica oficial do componente lite-apiserver no SuperEdge cobrindo proxy por Common Name X.509, motores de cache local e autonomia L3; consultado em 2026-10-03.
- [SuperEdge — Official GitHub Repository](https://github.com/superedge/superedge) — Repositório oficial Apache-2.0 do SuperEdge; consultado em 2026-10-03.
