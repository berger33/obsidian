---
id: software.devops.tranche10.000928
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md", "https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md", "https://github.com/bitnami-labs/sealed-secrets"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Bitnami Sealed Secrets: backup das chaves privadas de selamento, Disaster Recovery e descriptografia offline (--recovery-unseal)

## Em uma frase
Para recuperar um cluster destruído ou descriptografar `SealedSecret`s em caso de perda total do cluster, o administrador deve fazer backup dos Secrets de chaves privadas do controlador (`sealedsecrets.bitnami.com/sealed-secrets-key`), podendo restaurá-los em um novo cluster ou usá-los localmente com `kubeseal --recovery-unseal --recovery-private-key`.

## Por que importa
Se você tem todos os seus `SealedSecret`s versionados no Git, mas perde completamente o cluster Kubernetes (por exemplo, um disco `etcd` corrompido ou um cluster efêmero deletado por engano) **sem ter feito backup da chave privada do controlador**, ninguém no mundo conseguirá descriptografar os `SealedSecret`s que estão no Git! As seções `FAQ` (`How can I do a backup of my SealedSecrets?` e `Can I decrypt my secrets offline with a backup key?`) do README oficial alertam sobre isso.

## Como funciona
Para garantir a recuperação de desastres (Disaster Recovery): (1) **Backup da chave mestre**: após instalar o controlador (e periodicamente após renovações), o administrador faz backup dos Secrets de chave privada do controlador com **`kubectl get secret -n kube-system -l sealedsecrets.bitnami.com/sealed-secrets-key -o yaml > master-keys-backup.yaml`** e guarda esse arquivo em um cofre seguro fora do cluster; (2) **Restore em novo cluster**: ao recriar o cluster do zero, aplica-se `kubectl apply -f master-keys-backup.yaml` antes (ou reiniciando o controlador depois) para que o novo controlador consiga descriptografar todos os `SealedSecret`s existentes no Git; e (3) **Descriptografia de emergência offline**: caso o cluster não exista mais, usa-se **`kubeseal --recovery-unseal --recovery-private-key master-keys-backup.yaml < mysealedsecret.yaml`**.

## Exemplo
```bash
# Fazer backup das chaves de selamento do controlador e testar a descriptografia de recuperação offline
kubectl get secret -n kube-system -l sealedsecrets.bitnami.com/sealed-secrets-key -o yaml > /tmp/sealed-master.key
kubeseal --recovery-unseal --recovery-private-key /tmp/sealed-master.key -o yaml < mysealedsecret.yaml
```

## Limites e trade-offs
O arquivo `master-keys-backup.yaml` contém as chaves privadas RSA em texto claro (codificadas apenas em base64) que abrem **todos** os `SealedSecret`s daquele cluster; trate esse arquivo de backup com o mesmo nível de proteção de uma chave raiz de CA (criptografando-o com GPG/SOPS ou guardando em um cofre de hardware/nuvem restrito a administradores) e nunca o coloque em texto claro no repositório Git.

## Como verificar
Em um ambiente de homologação, teste o comando `kubeseal --recovery-unseal --recovery-private-key /tmp/sealed-master.key < mysealedsecret.yaml` para validar que seu procedimento de Disaster Recovery recupera o `Secret` original.

## Conexões
- [[sealedsecrets-criptografia-hibrida-aes-gcm-rsa-oaep-detalhes]] — Veja também: Bitnami Sealed Secrets: funcionamento interno da criptografia híbrida (AES-256-GCM + RSA-OAep-SHA256).
- [[sealedsecrets-gke-privado-firewall-8080-warden-service-proxier]] — Veja também: Bitnami Sealed Secrets: operação em clusters GKE privados (firewall 8080/8081) e restrições do GKE Warden (system:authenticated).
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Referência cruzada direta com sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd.
- [[sealedsecrets-rotacao-chaves-sealing-key-renewal-re-encrypt]] — Referência cruzada direta com sealedsecrets-rotacao-chaves-sealing-key-renewal-re-encrypt.
- [[talos-bootstrap-etcd-gerenciamento-control-plane-ha]] — Referência cruzada direta com talos-bootstrap-etcd-gerenciamento-control-plane-ha.

## Fontes
- [Bitnami Sealed Secrets GitHub — README.md (kubeseal, SealedSecret Template, Scopes, Key Renewal & AES-GCM/RSA-OAEP Crypto)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md) — README oficial do Bitnami Sealed Secrets detalhando funcionamento de kubeseal, spec.template, escopos strict/namespace-wide/cluster-wide, rotação de chaves de 30 dias, --merge-into, --recovery-unseal e criptografia híbrida; consultado em 2026-10-03.
- [Bitnami Sealed Secrets Documentation — GKE Guide (Private GKE Firewall 8080/8081 & GKE Warden serviceProxier Restrictions)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md) — Guia oficial de implantação no GKE documentando selamento offline, regras de firewall para clusters privados e contorno da restrição do GKE Warden (1.32.2+) sobre system:authenticated; consultado em 2026-10-03.
- [Bitnami Sealed Secrets — Official GitHub Repository](https://github.com/bitnami-labs/sealed-secrets) — Repositório oficial Apache-2.0 do Bitnami Sealed Secrets; consultado em 2026-10-03.
