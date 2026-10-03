---
id: software.devops.tranche10.000927
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

# Bitnami Sealed Secrets: funcionamento interno da criptografia híbrida (AES-256-GCM + RSA-OAep-SHA256)

## Em uma frase
Internamente, cada item de `encryptedData` em um `SealedSecret` é protegido por criptografia híbrida combinando uma chave de sessão simétrica **AES-256-GCM** de 32 bytes gerada aleatoriamente com a cifragem dessa chave via **RSA-OAEP com SHA-256** usando o certificado do controlador.

## Por que importa
Compreender o esquema criptográfico subjacente (detalhado na seção `Details (advanced) -> Crypto` do README oficial) explica por que os valores cifrados no `SealedSecret` mudam a cada execução do `kubeseal` mesmo para a mesma senha, por que não há limite de tamanho para arquivos grandes no `Secret` e como o escopo (`namespace`/`name`) é matematicamente autenticado.

## Como funciona
Quando o `kubeseal` cifra um valor de `Secret`: (1) gera uma chave de sessão aleatória de 32 bytes (256 bits); (2) criptografa o valor do segredo com **AES-256-GCM** usando essa chave de sessão e um nonce zerado (seguro porque cada item usa uma chave de 32 bytes única gerada na hora); (3) criptografa a chave de sessão AES com a chave pública **RSA** do controlador usando **RSA-OAEP com SHA-256**, passando a string `<namespace>/<name>` (no escopo `strict`), `<namespace>` (no escopo `namespace-wide`) ou vazio (no escopo `cluster-wide`) como o parâmetro **`label` (Additional Authenticated Data)** do OAEP; e (4) concatena o tamanho da chave RSA cifrada (2 bytes big-endian) + ciphertext RSA + ciphertext AES-GCM e codifica tudo em Base64.

## Exemplo
```bash
# Inspecionar o certificado X.509 RSA público usado pelo controlador do Sealed Secrets para a cifragem RSA-OAEP
kubeseal --fetch-cert | openssl x509 -noout -text | grep -A 2 "Public Key Algorithm"
```

## Limites e trade-offs
Como o `kubeseal` gera uma chave de sessão AES-256 aleatória nova toda vez que é executado, rodar `kubeseal` novamente sobre um arquivo `secret.yaml` inalterado produzirá strings `encryptedData` completamente diferentes a cada execução (gerando diffs desnecessários no Git); para evitar sujar o histórico do Git nas chaves que não mudaram, use sempre `kubeseal --merge-into` apenas para a chave alterada.

## Como verificar
Execute `kubeseal --cert cluster-pub-cert.pem < secret.yaml` duas vezes seguidas para o mesmo arquivo de entrada e observe que o Base64 de `encryptedData` muda a cada execução devido à nova chave de sessão aleatória.

## Conexões
- [[sealedsecrets-atualizacao-merge-into-raw-mode-validacao]] — Veja também: Bitnami Sealed Secrets: adição de itens sem conhecer chaves antigas (--merge-into), modo --raw e validação (--validate).
- [[sealedsecrets-backup-chaves-privadas-recovery-offline-unseal]] — Veja também: Bitnami Sealed Secrets: backup das chaves privadas de selamento, Disaster Recovery e descriptografia offline (--recovery-unseal).
- [[sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd]] — Referência cruzada direta com sealedsecrets-criptografia-assimetrica-gitops-kubeseal-crd.
- [[sealedsecrets-escopos-criptografia-strict-namespace-wide-cluster-wide]] — Referência cruzada direta com sealedsecrets-escopos-criptografia-strict-namespace-wide-cluster-wide.
- [[sops-criptografia-parcial-chaves-encrypted-regex-mac]] — Referência cruzada direta com sops-criptografia-parcial-chaves-encrypted-regex-mac.

## Fontes
- [Bitnami Sealed Secrets GitHub — README.md (kubeseal, SealedSecret Template, Scopes, Key Renewal & AES-GCM/RSA-OAEP Crypto)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/README.md) — README oficial do Bitnami Sealed Secrets detalhando funcionamento de kubeseal, spec.template, escopos strict/namespace-wide/cluster-wide, rotação de chaves de 30 dias, --merge-into, --recovery-unseal e criptografia híbrida; consultado em 2026-10-03.
- [Bitnami Sealed Secrets Documentation — GKE Guide (Private GKE Firewall 8080/8081 & GKE Warden serviceProxier Restrictions)](https://raw.githubusercontent.com/bitnami-labs/sealed-secrets/main/docs/GKE.md) — Guia oficial de implantação no GKE documentando selamento offline, regras de firewall para clusters privados e contorno da restrição do GKE Warden (1.32.2+) sobre system:authenticated; consultado em 2026-10-03.
- [Bitnami Sealed Secrets — Official GitHub Repository](https://github.com/bitnami-labs/sealed-secrets) — Repositório oficial Apache-2.0 do Bitnami Sealed Secrets; consultado em 2026-10-03.
