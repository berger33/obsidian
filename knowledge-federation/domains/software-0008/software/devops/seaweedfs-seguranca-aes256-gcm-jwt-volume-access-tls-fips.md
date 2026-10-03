---
id: software.devops.tranche18.001730
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
fontes: ["https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/README.md", "https://raw.githubusercontent.com/seaweedfs/seaweedfs-csi-driver/master/README.md", "https://github.com/seaweedfs/seaweedfs"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SeaweedFS: segurança em repouso e trânsito com criptografia AES-256-GCM no Filer, mTLS, JWT Volume Access e builds FIPS

## Em uma frase
O SeaweedFS implementa múltiplas camadas de segurança de infraestrutura: criptografia em repouso **AES-256-GCM** no Filer, **TLS/mTLS** entre Master, Volume e Filer, controle de acesso a volumes assinado por **JWT** e binários compatíveis com **FIPS**.

## Por que importa
Como os clientes e Filers falam diretamente com os Volume Servers para obter desempenho máximo sem passar pelo Master, é necessário impedir que um cliente não autorizado na rede interna leia ou sobrescreva `file ids` diretamente na porta de um Volume Server.

## Como funciona
No arquivo `security.toml`, o administrador configura os certificados mTLS para comunicação gRPC entre componentes e a chave de assinatura JWT (`jwt.signing`). Assim, toda operação de escrita/leitura em um Volume Server exige um token JWT de curta duração emitido pelo Master ou Filer, enquanto o Filer cifra os blocos de dados com AES-256-GCM usando chaves únicas por arquivo.

## Exemplo
```toml
# /etc/seaweedfs/security.toml
[jwt.signing]
key = "chave-secreta-jwt-escrita-clusters"
expires_after_seconds = 10

[jwt.signing.read]
key = "chave-secreta-jwt-leitura-clusters"
expires_after_seconds = 60
```

## Limites e trade-offs
Para habilitar TLS no `seaweedfs-csi-driver` no Kubernetes, utilize o Helm chart configurando `tlsSecret` com os certificados para que os DaemonSets `seaweedfs-mount` e `seaweedfs-node` montem as credenciais TLS automaticamente.

## Como verificar
Teste uma requisição direta sem token JWT contra a porta de um Volume Server e confirme que o acesso é negado quando `security.toml` está ativo.

## Conexões
- [[seaweedfs-csi-driver-cotas-capacidade-collection-enospc-safe-rollout]] — Veja também: SeaweedFS CSI Driver: aplicação de cotas de capacidade (`ENOSPC`) por `collection` e procedimento de *Safe Rollout*.

## Fontes
- [SeaweedFS GitHub — README.md (O(1) Disk Read Blob Store, Master/Volume/Filer, S3 API, S3 Tables Iceberg/Lance, Cloud Drive & Erasure Coding)](https://raw.githubusercontent.com/seaweedfs/seaweedfs/master/README.md) — README oficial do seaweedfs/seaweedfs detalhando leitura em 1 seek (16-byte RAM index), replicação XYZ, Filer stateless, S3 Gateway e Lakehouse; consultado em 2026-10-03.
- [SeaweedFS CSI Driver GitHub — README.md (Kubernetes CSI Dynamic/Static Provisioning, Collection Quotas & Safe Rollout)](https://raw.githubusercontent.com/seaweedfs/seaweedfs-csi-driver/master/README.md) — Documentação oficial do seaweedfs-csi-driver cobrindo provisionamento RWX, cotas ENOSPC por collection, parâmetros de StorageClass e atualização OnDelete; consultado em 2026-10-03.
- [SeaweedFS — Official GitHub Repository](https://github.com/seaweedfs/seaweedfs) — Repositório oficial Apache-2.0 do SeaweedFS; consultado em 2026-10-03.
