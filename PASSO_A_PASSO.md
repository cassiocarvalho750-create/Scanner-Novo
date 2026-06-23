# Scanner na nuvem — passo a passo (GitHub)

O scanner vai rodar sozinho às **13h, 16h e 19h (Brasília), de segunda a sexta**,
e publicar um site que você abre no celular. Você não precisa deixar o PC ligado.

## O que você vai fazer (uma vez só)

### 1. Criar o repositório
1. Entre no GitHub (você já tem conta).
2. Clique em **New repository** (botão verde, ou em https://github.com/new).
3. Nome: `scanner` (ou o que preferir).
4. Marque **Public** (necessário para o site gratuito do GitHub Pages).
5. Clique em **Create repository**.

### 2. Subir os arquivos
1. Na página do repositório novo, clique em **uploading an existing file**
   (ou **Add file → Upload files**).
2. Arraste **TODOS** os arquivos desta pasta para a área de upload, INCLUSIVE
   a pasta `.github` (ela contém o agendador). 
   - Dica: se o navegador não deixar arrastar a pasta `.github`, veja a seção
     "Se a pasta .github não subir" no final.
3. Escreva qualquer descrição em "Commit changes" e clique no botão verde
   **Commit changes**.

### 3. Ligar o GitHub Pages
1. No repositório, vá em **Settings** (engrenagem no topo).
2. No menu da esquerda, clique em **Pages**.
3. Em "Build and deployment" → "Source", escolha **Deploy from a branch**.
4. Em "Branch", escolha **gh-pages** e pasta **/ (root)**, clique **Save**.
   - OBS: a branch `gh-pages` só aparece DEPOIS que o scanner rodar a 1a vez
     (passo 4). Se não aparecer ainda, faça o passo 4 primeiro e volte aqui.

### 4. Rodar a primeira vez (sem esperar o horário)
1. No repositório, vá na aba **Actions**.
2. Se aparecer um aviso amarelo pedindo para habilitar workflows, clique em
   **I understand my workflows, go ahead and enable them**.
3. Clique no workflow **Scanner DIDI ADX BB** na lista à esquerda.
4. Clique em **Run workflow** (botão à direita) → **Run workflow**.
5. Espere alguns minutos (varre os dois mercados). Quando ficar verde, terminou.
6. Volte ao passo 3 (Pages) se a branch `gh-pages` ainda não estava disponível.

### 5. Abrir no celular
- O endereço do seu site é:
  **https://SEU_USUARIO.github.io/scanner/**
  (troque SEU_USUARIO pelo seu nome de usuário do GitHub, e `scanner` pelo nome
  que você deu ao repositório).
- Abra esse link no navegador do celular e **adicione à tela inicial**
  (menu do navegador → "Adicionar à tela de início"). Vira quase um app.

## Pronto!
A partir daí ele roda sozinho 3x ao dia, seg–sex. Sempre que abrir o link,
verá o resultado mais recente, com o horário da última atualização no topo.

---

## Se a pasta .github não subir pelo navegador
O GitHub às vezes esconde pastas que começam com ponto. Alternativa:
1. No repositório, clique **Add file → Create new file**.
2. No nome do arquivo, digite exatamente:
   `.github/workflows/scanner.yml`
   (ao digitar as barras, o GitHub cria as pastas sozinho).
3. Cole todo o conteúdo do arquivo `scanner.yml` (abra o que está nesta pasta
   com o Bloco de Notas e copie tudo).
4. Clique **Commit changes**.

## Horários (para referência)
- 13h, 16h, 19h Brasília = 16h, 19h, 22h UTC.
- Estão no arquivo `.github/workflows/scanner.yml`, linha do `cron`.
- Para mudar, edite os números das horas UTC (lembre: Brasília + 3 = UTC).
