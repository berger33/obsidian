---
id: software.seguranca.tranche14.001398
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md", "https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Memória Não-Volátil (**NVRAM**: `tpm2_nvdefine`, `tpm2_nvwrite`, `tpm2_nvread`) e **Contadores Monotônicos Anti-Rollback (`tpm2_nvincrement`)** no TPM 2.0

## Em uma frase
Imagine que um atacante com acesso físico ao disco de um servidor faça uma cópia completa da imagem do disco hoje (versão 10 da configuração/política), espere você revogar uma credencial ou atualizar uma política de segurança amanhã (versão 11) e então **restaure a imagem antiga do disco de ontem (versão 10)** para ressuscitar a versão vulnerável (**Rollback Attack / Replay de Estado de Disco**)! Como o chip **TPM 2.0** impede ataques de Rollback de disco ou de políticas?

## Por que importa
Usando a **Memória Não-Volátil Segura (`NVRAM`)** e os **Contadores Monotônicos de Hardware (`nt=counter` via `tpm2_nvdefine` e `tpm2_nvincrement`)** dentro do próprio chip TPM!

## Como funciona
Um índice de NVRAM do tipo **`counter`** dentro do TPM 2.0 possui uma propriedade garantida pelo silício: **ele só pode ser incrementado (`+1` via `tpm2_nvincrement`) e JAMAIS pode ser decrementado ou zerado para um número menor**, mesmo que o sistema operacional inteiro seja formatado ou o disco seja substituído por um backup antigo! Ao incluir o valor do contador monotônico (ou um segredo atualizado em NVRAM) na política de selagem (`TPM2_PolicyNV`), qualquer tentativa de dar boot com um estado de disco antigo falha imediatamente!

## Exemplo
```bash
# Definir um Contador Monotonico de 8 bytes na NVRAM do TPM 2.0 (indice 0x01500016), incrementa-lo com tpm2_nvincrement e ler o valor atual
tpm2_nvdefine 0x01500016 -C o -s 8 -a "ownerwrite|ownerread|nt=counter"
tpm2_nvincrement 0x01500016 -C o
tpm2_nvread 0x01500016 -C o | xxd
tpm2_getcap handles-nv-index
```

## Limites e trade-offs
Além do tipo `counter` (*Monotonic Counter*), os índices de NVRAM do TPM (`tpm2_nvdefine`) também suportam os modos: **`ordinary`** (armazena até alguns kilobytes de dados arbitrários, como uma semente LUKS, certificado de fábrica ou hash raiz de configuração), **`bits`** (campo de flags onde bits individuais só podem ser ligados `1` com `tpm2_nvsetbits`) e **`extend`** (um índice NVRAM que funciona exatamente como um PCR persistente via `tpm2_nvextend`!)!

## Como verificar
Use **`tpm2_nvwritelock`** e **`tpm2_nvreadlock`** (com os atributos `writedefine` / `read_stclear`) quando quiser travar um índice de NVRAM após a inicialização do boot até o próximo reset físico da máquina!

## Conexões
- [[tpm2-pkcs11-ssh-tls-nginx-openvpn-chaves-hardware-nao-exportaveis]] — Veja também: Uso de Chaves TPM 2.0 Não-Exportáveis em **OpenSSH, Nginx, OpenVPN, StrongSwan e Rust/Go** com **`tpm2-pkcs11`** e **`tpm2-openssl` Provider**.
- [[tpm2-protecao-forca-bruta-dictionary-attack-lockout-clear-seguranca]] — Veja também: Proteção Contra Força Bruta em Hardware (**Dictionary Attack Lockout**: `tpm2_dictionarylockout`), Senhas de Hierarquia (`tpm2_changeauth`) e **TRNG (`tpm2_getrandom`)**.
- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Referência cruzada direta com tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs.
- [[tpm2-politicas-avancadas-ea-policyauthorize-policysigned-policyor-pin]] — Referência cruzada direta com tpm2-politicas-avancadas-ea-policyauthorize-policysigned-policyor-pin.

## Fontes
- [Official `tpm2-tools` GitHub Repository (`tpm2-software/tpm2-tools`)](https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md) — repositório oficial dos utilitários `tpm2-tools` cobrindo criação de chaves, selagem em PCRs, políticas EA, cotações de atestação remota (`tpm2_quote`), NVRAM e Dictionary Attack Lockout; consultado em 2026-10-03.
- [Official TCG TPM2 Software Stack (`tpm2-software/tpm2-tss`) GitHub Repository](https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md) — documentação oficial da pilha `tpm2-tss` detalhando as camadas arquiteturais `libtss2-fapi`, `libtss2-esys`, `libtss2-sys`, `libtss2-mu` e módulos `TCTI` (`device`, `swtpm`, `mssim`, `tctildr`); consultado em 2026-10-03.
