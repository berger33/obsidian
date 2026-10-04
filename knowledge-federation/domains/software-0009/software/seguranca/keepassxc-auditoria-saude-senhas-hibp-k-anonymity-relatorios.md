---
id: software.seguranca.tranche13.001209
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/README.md", "https://keepassxc.org/docs/KeePassXC_UserGuide"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Auditoria de Saúde Criptográfica do Cofre (**Database Reports**): Verificação Privada **HaveIBeenPwned (`k-Anonymity`)**, Reuso e Entropia

## Em uma frase
Ter um cofre criptografado com Argon2id e YubiKey não protege uma aplicação externa se a senha guardada dentro daquela entrada for fraca, reutilizada em 5 serviços diferentes ou já tiver vazado em algum incidente público!

## Por que importa
O módulo **Database Reports (`Ctrl+Shift+R`)** e o subcomando **`keepassxc-cli analyze`** auditam todas as entradas do cofre em busca de: **(1) Senhas reutilizadas** em múltiplas entradas, **(2) Senhas fracas ou curtas** (avaliadas pelo estimador de entropia em bits), **(3) Entradas expiradas** e **(4) Verificação contra o banco HaveIBeenPwned (HIBP) preservando 100% da privacidade via modelo `k-Anonymity`**!

## Como funciona
Como funciona a checagem **HIBP `k-Anonymity`**? O KeePassXC calcula localmente o hash `SHA-1` de cada senha e envia para a API do HIBP **apenas os primeiros 5 caracteres hexadecimais do hash (`prefixo de 20 bits`)**; a API devolve centenas de sufixos que começam com aqueles 5 caracteres, e o KeePassXC verifica localmente em memória se o hash completo da sua senha está na lista — **sem que sua senha ou seu hash completo jamais saia do seu computador**!

## Exemplo
```bash
# Auditar a qualidade e entropia das senhas de um cofre KDBX via keepassxc-cli (sem enviar dados para a rede)
keepassxc-cli analyze ./cofre-infraestrutura.kdbx
keepassxc-cli diceware -W 7
```

## Limites e trade-offs
Ao gerar novas senhas para serviços críticos ou chaves mestras de novos cofres, utilize o gerador de **Passphrases Diceware (`keepassxc-cli diceware -W 7`)** (7 palavras sorteadas da lista EFF proporcionam ~90 bits de entropia pura e são fáceis de digitar e memorizar) ou senhas aleatórias de 24 a 32 caracteres!

## Como verificar
Use as **Referências de Campo (*Field References*, ex.: `{REF:P@I:UUID_DA_ENTRADA_ORIGINAL}`)** quando duas entradas diferentes no cofre usarem legitimamente a mesma conta de SSO/Active Directory: assim a senha existe em um único lugar e o relatório de saúde não acusa falso positivo de duplicação!

## Conexões
- [[keepassxc-compartilhamento-equipes-keeshare-assinatura-merge-git]] — Veja também: Compartilhamento Seguro de Cofres em Equipe com **KeeShare** (Contêineres Assinados) e Resolução de Conflitos com **`keepassxc-cli merge`**.
- [[keepassxc-hardening-memoria-protecao-process-dump-cve-2023-35866]] — Veja também: Segurança de Memória em Gerenciadores de Senhas Desktop: Lições do **`keepass-password-dumper` (`CVE-2023-35866`)**, `prctl(PR_SET_DUMPABLE)` e Isolamento.
- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Referência cruzada direta com keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256.
- [[keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura]] — Referência cruzada direta com keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura.
- [[pam-qualidade-senhas-pam-pwquality-entropia-dicionario-historico]] — Referência cruzada direta com pam-qualidade-senhas-pam-pwquality-entropia-dicionario-historico.

## Fontes
- [KeePassXC Official GitHub — Cross-Platform Community-Driven Port of Keepass](https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/README.md) — repositório oficial do KeePassXC cobrindo criptografia KDBX 4 (AES-256, Twofish, ChaCha20), YubiKey/OnlyKey, `keepassxc-cli`, SSH Agent e Secret Service; consultado em 2026-10-03.
- [KeePassXC Official User Guide (`keepassxc.org/docs/KeePassXC_UserGuide`)](https://keepassxc.org/docs/KeePassXC_UserGuide) — guia oficial do usuário do KeePassXC detalhando Auto-Type, integração com navegador, Passkeys, KeeShare, Database Reports (HIBP) e proteção de memória/tela; consultado em 2026-10-03.
