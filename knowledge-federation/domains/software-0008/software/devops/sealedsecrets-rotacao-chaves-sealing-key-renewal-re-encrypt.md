---
id: software.devops.tranche10.000925
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

# Bitnami Sealed Secrets: renovação periódica de chaves de selamento (30 dias), rotação de segredos e re-encryption

## Em uma frase
O controlador do Sealed Secrets gera uma nova chave de selamento a cada 30 dias mantendo todas as chaves privadas históricas em um registro (`sealed-secrets-key*` no cluster), mas a segurança máxima após um vazamento exige rotacionar a credencial real do usuário além de rodar `kubeseal --re-encrypt`.

## Por que importa
Uma dúvida recorrente em auditorias de segurança (documentada na seção `Secret Rotation -> Common misconceptions about key renewal` do README oficial) é achar que a renovação automática de chaves de 30 dias do controlador invalida sozinha `SealedSecret`s antigos vazados no Git ou dispensa a rotação das senhas reais das aplicações.

## Como funciona
O controlador armazena suas chaves criptográficas em Secrets no seu próprio namespace (marcados com a label **`sealedsecrets.bitnami.com/sealed-secrets-key: active`**). A cada **30 dias** (configurável via `--key-renew-period`), o controlador cria um novo par de chaves para novas operações do `kubeseal`, mas **mantém todas as chaves privadas antigas** na memória para que todos os `SealedSecret`s existentes no Git continuem sendo descriptografados sem quebrar o cluster. Caso uma chave antiga precise ser aposentada, usa-se **`kubeseal --re-encrypt < old-sealed.yaml > new-sealed.yaml`** (que pede ao controlador para recifrar os dados com a chave ativa mais recente sem expor o texto claro ao cliente) antes de apagar a chave privada antiga do cluster.

## Exemplo
```bash
# Listar todas as chaves de selamento armazenadas no namespace do controlador e re-criptografar um SealedSecret com a chave mais recente
kubectl get secret -n kube-system -l sealedsecrets.bitnami.com/sealed-secrets-key
kubeseal --re-encrypt -o yaml < mysealedsecret.yaml > mysealedsecret-renewed.yaml
```

## Limites e trade-offs
Conforme enfatiza o README oficial, se alguém comprometer uma chave privada antiga do controlador ou se um segredo for exposto, apenas re-criptografar o `SealedSecret` (`--re-encrypt`) **não** protege a senha antiga que já pôde ser lida: a rotação real do segredo (`User secret rotation`) exige gerar uma **nova senha/chave de API** no serviço externo e selá-la novamente com `kubeseal`.

## Como verificar
Execute `kubectl get secret -n kube-system -l sealedsecrets.bitnami.com/sealed-secrets-key` para verificar os certificados e datas de criação das chaves de selamento ativas no seu cluster.

## Conexões
- [[sealedsecrets-certificado-publico-fetch-cert-offline-url]] — Veja também: Bitnami Sealed Secrets: obtenção da chave pública (--fetch-cert) e selamento offline (--cert e SEALED_SECRETS_CERT).
- [[sealedsecrets-atualizacao-merge-into-raw-mode-validacao]] — Veja também: Bitnami Sealed Secrets: adição de itens sem conhecer chaves antigas (--merge-into), modo --raw e validação (--validate).
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Referência cruzada direta com sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd.
- [[sealedsecrets-backup-chaves-privadas-recovery-offline-unseal]] — Referência cruzada direta com sealedsecrets-backup-chaves-privadas-recovery-offline-unseal.

## Fontes
- [Bitnami Sealed Secrets GitHub — README.md (kubeseal, SealedSecret Template, Scopes, Key Renewal & AES-GCM/RSA-OAEP Crypto)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md) — README oficial do Bitnami Sealed Secrets detalhando funcionamento de kubeseal, spec.template, escopos strict/namespace-wide/cluster-wide, rotação de chaves de 30 dias, --merge-into, --recovery-unseal e criptografia híbrida; consultado em 2026-10-03.
- [Bitnami Sealed Secrets Documentation — GKE Guide (Private GKE Firewall 8080/8081 & GKE Warden serviceProxier Restrictions)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md) — Guia oficial de implantação no GKE documentando selamento offline, regras de firewall para clusters privados e contorno da restrição do GKE Warden (1.32.2+) sobre system:authenticated; consultado em 2026-10-03.
- [Bitnami Sealed Secrets — Official GitHub Repository](https://github.com/bitnami-labs/sealed-secrets) — Repositório oficial Apache-2.0 do Bitnami Sealed Secrets; consultado em 2026-10-03.
