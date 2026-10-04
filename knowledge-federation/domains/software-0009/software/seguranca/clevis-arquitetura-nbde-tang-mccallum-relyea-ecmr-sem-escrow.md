---
id: software.seguranca.tranche08.000731
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

# Clevis & Tang (**NBDE — *Network-Bound Disk Encryption***): Arquitetura Criptográfica *Stateless* com Troca **McCallum-Relyea (`ECMR`)** sem Key Escrow

## Em uma frase
**Clevis** (`latchset/clevis`, cliente plugável de decriptação automatizada) e **Tang** (`latchset/tang`, servidor de vinculação criptográfica à presença na rede), ambos baseados na biblioteca C **`jose`** (JOSE/JWE/JWK/JWS), formam a solução padrão do Linux corporativo (RHEL, Fedora, Debian, Ubuntu) para **Network-Bound Disk Encryption (NBDE)**.

## Por que importa
Em um datacenter com centenas de servidores físicos criptografados com LUKS2, digitar senhas manualmente no console KVM/iDRAC de 500 servidores após uma manutenção elétrica é inviável; por outro lado, usar um servidor tradicional de *Key Escrow* (que guarda todas as chaves dos servidores em um banco de dados) cria um alvo catastrófico.

## Como funciona
Conforme explica o `README.md` oficial do **Tang**, o protocolo usa a troca de chaves elípticas **McCallum-Relyea (`ECMR`)**: **o servidor Tang é 100% *stateless*, não armazena nenhuma chave de cliente, não sabe quais clientes existem e nunca vê a chave de criptografia do cliente em momento algum**! O cliente Clevis mascara sua chave efêmera com uma chave de cegamento (*blinding key*) antes do `POST /rec/<kid>`, de modo que apenas um cliente fisicamente presente na rede segura que alcance o servidor Tang consegue remover o cegamento e reconstruir a chave do LUKS2.

## Exemplo
```bash
# Habilitar o socket do servidor Tang (systemd socket activation) e inspecionar o anuncio JWS de chaves publicas
sudo systemctl enable --now tangd.socket
curl -sS http://127.0.0.1/adv | jose fmt -j- -Sy -o- | jq .
```

## Limites e trade-offs
Como enfatiza a documentação oficial do Tang, **jamais armazene as chaves privadas do servidor Tang (`/var/db/tang/*.jwk`) dentro do mesmo disco físico ou cluster de armazenamento que depende daquele próprio servidor Tang para desbloquear no boot**!

## Como verificar
Verifique em `/var/db/tang/` a geração automática do par de chaves de assinatura (`ES512`) e derivação (`ECMR`).

## Conexões
- [[clevis-operacao-servidor-tang-rotacao-chaves-jwk-adv-verificacao]] — Veja também: Tang Server: Operação de `/var/db/tang/`, Thumbprints **JWK (`S256`)** e **Rotação Graciosa de Chaves (`jose jwk gen`)** sem Quebrar o Boot.
- [[clevis-politicas-quorum-shamir-secret-sharing-sss-tang-tpm2]] — Referência cruzada direta com clevis-politicas-quorum-shamir-secret-sharing-sss-tang-tpm2.
- [[cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup]] — Referência cruzada direta com cryptsetup-arquitetura-dm-crypt-luks2-veritysetup-integritysetup.

## Fontes
- [Clevis Official GitHub — Automated Decryption Framework & Pins (tang, tpm2, sss, pkcs11)](https://raw.githubusercontent.com/latchset/clevis/master/README.md) — documentação oficial do framework Clevis cobrindo pins tang, tpm2, sss (Shamir Secret Sharing), pkcs11 e integração LUKS2/initramfs; consultado em 2026-10-03.
- [Tang Official GitHub — Stateless Network-Bound Cryptographic Server & ECMR Protocol](https://raw.githubusercontent.com/latchset/tang/master/README.md) — documentação oficial do servidor Tang cobrindo protocolo McCallum-Relyea (ECMR), geração/rotação de chaves JWK e operação stateless; consultado em 2026-10-03.
- [Latchset JOSE Official C Library & CLI Reference](https://github.com/latchset/jose) — repositório oficial da biblioteca e utilitário jose para objetos JWE/JWK/JWS utilizados pelo Clevis e Tang; consultado em 2026-10-03.
