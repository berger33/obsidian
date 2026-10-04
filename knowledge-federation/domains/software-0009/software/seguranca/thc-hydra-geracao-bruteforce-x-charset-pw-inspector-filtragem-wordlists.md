---
id: software.seguranca.tranche16.001577
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README", "https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Geração On-the-Fly (**`-x min:max:charset`**) e Filtragem de Wordlists por Política de Senha com o Utilitário **`pw-inspector`** do THC-Hydra

## Em uma frase
Imagine que durante uma auditoria de segurança você descobre a política exata de senhas do sistema alvo: por exemplo, o sistema **exige obrigatoriamente que toute senha tenha no mínimo 8 caracteres, pelo menos 1 letra maiúscula, 1 letra minúscula e 1 número**. Se a sua wordlist tiver 10.000 senhas, mas 7.000 delas tiverem apenas 6 caracteres ou forem só letras minúsculas, testar essas 7.000 senhas na rede é um **desperdício total de conexões e barulho nos logs**!

## Por que importa
Como filtrar qualquer wordlist para manter **apenas as senhas que atendem exatamente à política de complexidade do alvo** antes de rodar o Hydra?

## Como funciona
Usando o utilitário companheiro oficial que já vem instalado junto com o THC-Hydra (citado na seção `SEE ALSO` da manpage `hydra(1)`): o **`pw-inspector`**! O `pw-inspector` lê uma lista de senhas (de um arquivo `-i` ou `stdin` via pipe) e filtra por tamanho mínimo (`-m 8`), tamanho máximo (`-M 16`) e conjuntos de caracteres exigidos (`-c N`: minúsculas `-l`, maiúsculas `-u`, números `-n`, imprimíveis `-p`, especiais `-s`)!

## Exemplo
```bash
# Usar o utilitario oficial pw-inspector do pacote THC-Hydra para filtrar uma wordlist mantendo apenas senhas com >= 8 chars e 3 classes (a, A, 1)
pw-inspector -i ./wordlist_bruta.txt -o ./wordlist_politica_ad.txt -m 8 -M 20 -c 3 -l -u -n
wc -l ./wordlist_bruta.txt ./wordlist_politica_ad.txt
```

## Limites e trade-offs
Veja como o **`pw-inspector`** acima reduz drasticamente o número de tentativas de rede em um teste autorizado: ao passar `-m 8 -c 3 -l -u -n`, ele descarta instantaneamente qualquer candidato com menos de 8 caracteres ou que não combine pelo menos 3 das classes solicitadas (minúsculas `-l`, maiúsculas `-u`, números `-n`), garantindo que **100% dos pacotes enviados pelo Hydra na rede testem senhas válidas perante a política do sistema**!

## Como verificar
E para casos específicos de PINs curtos ou senhas geradas por máscara curta sem arquivo externo, a manpage `hydra(1)` também documenta o gerador interno **`-x min:max:charset`** (onde `a` = minúsculas, `A` = maiúsculas, `1` = dígitos; ex.: `-x 4:4:1` para PINs numéricos de 4 dígitos).

## Conexões
- [[thc-hydra-auditoria-protocolos-infraestrutura-ssh-sshkey-rdp-smb-snmp]] — Veja também: Auditando Protocolos de Infraestrutura e Gerência no THC-Hydra: **`ssh` / `sshkey`**, **`rdp`**, **`smb`**, **`snmp` (Community Strings v1/v2c/v3)** e **`cisco-enable`**.
- [[thc-hydra-auditoria-email-diretorio-smtp-enum-imap-pop3-ldap-tls]] — Veja também: Auditando Serviços de E-mail e Diretório no THC-Hydra: Enumeração de Contas **`smtp-enum` (`VRFY`/`EXPN`/`RCPT TO`)**, **`smtp`**, **`imap`/`pop3`** e **`ldap3` (`-S` LDAPS)**.
- [[thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos]] — Referência cruzada direta com thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos.
- [[thc-hydra-modos-credenciais-password-spraying-u-colon-file-e-nsr]] — Referência cruzada direta com thc-hydra-modos-credenciais-password-spraying-u-colon-file-e-nsr.
- [[john-modo-wordlist-regras-mangling-rules-best64-korelogic-custom]] — Referência cruzada direta com john-modo-wordlist-regras-mangling-rules-best64-korelogic-custom.

## Fontes
- [THC-Hydra Official Documentation (`vanhauser-thc/thc-hydra/master/README`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README) — documentação oficial do THC-Hydra detalhando protocolos suportados, sintaxe URI `PROTOCOL://TARGET:PORT/OPTIONS`, listas `-M` e inspeção de módulos `hydra -U`; consultado em 2026-10-03.
- [Official `hydra(1)` Manpage Specification (`vanhauser-thc/thc-hydra/master/hydra.1`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1) — manpage oficial `hydra(1)` detalhando flags `-l`/`-L`, `-p`/`-P`, `-C`, `-e nsr`, `-u`, `-f`/`-F`, `-t`/`-T`, `-w`/`-W`/`-c`, `-R`, `-b json` e o utilitário `pw-inspector`; consultado em 2026-10-03.
