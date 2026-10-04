---
id: software.seguranca.tranche08.000732
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/latchset/clevis/master/README.md", "https://raw.githubusercontent.com/latchset/tang/master/README.md", "https://github.com/latchset/jose"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Tang Server: Operação de `/var/db/tang/`, Thumbprints **JWK (`S256`)** e **Rotação Graciosa de Chaves (`jose jwk gen`)** sem Quebrar o Boot

## Em uma frase
O servidor **Tang** responde a apenas duas rotas HTTP REST baseadas no padrão JOSE: **`GET /adv` (ou `/adv/<skid>`)**, que devolve um objeto JWS contendo as chaves públicas ativas do servidor assinadas pela(s) chave(s) de assinatura `ES512`, e **`POST /rec/<kid>`**, que realiza a operação matemática `ECMR` com a chave privada de troca solicitada pelo cliente.

## Por que importa
Quando o administrador provisiona um cliente Clevis pela primeira vez (`clevis encrypt tang` ou `clevis luks bind`), o Clevis exibe o **Thumbprint SHA-256 (`thp`)** da chave de assinatura do Tang (de forma idêntica ao fingerprint de host do SSH) ou valida contra um arquivo de anúncio pré-confiado (`"adv": "..."` ou `"thp": "..."`).

## Como funciona
Para **rotacionar as chaves de um servidor Tang em produção sem quebrar o desbloqueio de nenhum servidor existente**, o `README.md` oficial do Tang define um processo seguro em três etapas: **(1)** gerar um novo par de chaves (`ES512` + `ECMR`) com `jose jwk gen` em `/var/db/tang/`, **(2)** renomear as chaves antigas adicionando um **ponto `.` na frente do nome do arquivo (`.oldkey.jwk`)** e **(3)** só excluir as chaves `.oldkey.jwk` depois que todos os clientes tiverem atualizado seus vínculos (`clevis luks regen`).

## Exemplo
```bash
# Calcular o thumbprint SHA-256 (S256) das chaves de assinatura ativas do servidor Tang e gerar novas chaves para rotacao
sudo jose jwk thp -i /var/db/tang/*.jwk
sudo jose jwk gen -i '{"alg":"ES512"}' -o /var/db/tang/newsig.jwk
sudo jose jwk gen -i '{"alg":"ECMR"}' -o /var/db/tang/newexc.jwk
```

## Limites e trade-offs
Por que renomear a chave antiga para `.oldexc.jwk` (arquivo oculto com ponto `.`) funciona tão bem? Porque o Tang **para de anunciar chaves ocultas (`.jwk`) no `GET /adv`** (fazendo todos os novos clientes usarem a chave nova), mas **continua respondendo a pedidos de recuperação `POST /rec/<kid>` para chaves ocultas `.jwk`**, garantindo que servidores antigos continuem dando boot normalmente até rodarem `clevis luks regen`!

## Como verificar
Teste renomear a chave antiga para `.old.jwk` e confirme com `curl -s http://127.0.0.1/adv` que apenas a chave nova é anunciada, enquanto `clevis decrypt` de um JWE antigo continua funcionando.

## Conexões
- [[clevis-arquitetura-nbde-tang-mccallum-relyea-ecmr-sem-escrow]] — Veja também: Clevis & Tang (**NBDE — *Network-Bound Disk Encryption***): Arquitetura Criptográfica *Stateless* com Troca **McCallum-Relyea (`ECMR`)** sem Key Escrow.
- [[clevis-criptografia-dados-pins-tang-tpm2-pkcs11-jwe-formato]] — Veja também: Clevis: Arquitetura de **Pins (`tang`, `tpm2`, `sss`, `pkcs11`)** e Criptografia de Segredos em Objetos **JWE (`clevis encrypt` / `clevis decrypt`)**.
- [[clevis-integracao-luks2-clevis-luks-bind-initramfs-dracut-systemd]] — Referência cruzada direta com clevis-integracao-luks2-clevis-luks-bind-initramfs-dracut-systemd.
- [[clevis-auditoria-regeneracao-clevis-luks-list-regen-unbind-edit]] — Referência cruzada direta com clevis-auditoria-regeneracao-clevis-luks-list-regen-unbind-edit.

## Fontes
- [Clevis Official GitHub — Automated Decryption Framework & Pins (tang, tpm2, sss, pkcs11)](https://raw.githubusercontent.com/latchset/clevis/master/README.md) — documentação oficial do framework Clevis cobrindo pins tang, tpm2, sss (Shamir Secret Sharing), pkcs11 e integração LUKS2/initramfs; consultado em 2026-10-03.
- [Tang Official GitHub — Stateless Network-Bound Cryptographic Server & ECMR Protocol](https://raw.githubusercontent.com/latchset/tang/master/README.md) — documentação oficial do servidor Tang cobrindo protocolo McCallum-Relyea (ECMR), geração/rotação de chaves JWK e operação stateless; consultado em 2026-10-03.
- [Latchset JOSE Official C Library & CLI Reference](https://github.com/latchset/jose) — repositório oficial da biblioteca e utilitário jose para objetos JWE/JWK/JWS utilizados pelo Clevis e Tang; consultado em 2026-10-03.
